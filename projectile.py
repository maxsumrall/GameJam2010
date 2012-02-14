#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 



#The phaser-bullet-laser things that the ships shoot

import pygame


class Projectile(object):
	
	def __init__(self,x=0,y=0,vx=0,vy=0,shot = 1,pic ="pictures/rock.png",nukeStatus = False,imgScale=1):
		
		self.outerX = 55/imgScale
		self.outerY = 65/imgScale
		
		#This control strcture makes one bullet shot from the left of the ship, and one shoot from the right side
		if(shot == 1):
			self.x = x - 15
		else:
			self.x = x + self.outerX
			
			
		self.y = y
		self.vx = vx
		self.vy = vy
		self.exist = True
		self.isNuke = nukeStatus

		
		#Creatre the pygame pic of the bullet
		self.projectilePic = pygame.image.load(pic).convert_alpha()
		self.projectilePic = pygame.transform.scale(self.projectilePic,(self.outerX,self.outerY))

	def xPos(self):
		return self.x
		
	def yPos(self):
		return self.y
		
	def hitShip(self):
		self.exist = False
		
	def update(self,screenHeight):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
		
		#check if it leaves the screen
		if (self.y  < 0) or (self.y > screenHeight):
			self.exist = False
			
	
	def getPic(self):
		return self.projectilePic
		
	def getRect(self):
		return  pygame.Rect(self.x,self.y,self.outerX,self.outerY)
	
	def nukeExplode(self, shipObjects,ship,screen):
		
		#make the nuke kill everything
		for ships in shipObjects:
			ships.exist = False
			self.exist=  False

	
			
