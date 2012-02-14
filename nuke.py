#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 
		
		
		
import pygame

class Nuke(object):
	def __init__(self, x=0,y=0,imgScale=1):
		self.x = x
		self.y = y
		
		self.outerX = 50/imgScale*1.5
		self.outerY = 50/imgScale*1.5
		self.exist = True
		
		#Picture of powerUp
		nukePicture = "pictures/kaboom.png"
		
		#pygame special pixel dance it likes to do with my pictures
		self.nukePic = pygame.image.load(nukePicture).convert_alpha()
		#Scale the picture
		self.nukePic = pygame.transform.scale(self.nukePic,(self.outerX,self.outerY))

	def isHit(self, player):
		#health upgrade
		self.exist = False
		player.hasNuke =  True	
		
	def getPic(self):
		return self.nukePic
		
	def getRect(self):
		return  pygame.Rect(self.x,self.y,self.outerX,self.outerY)
