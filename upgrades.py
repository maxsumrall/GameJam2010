#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 



import pygame
class HealthPowerUp(object):
	def __init__(self, x=0,y=0,imgScale=1):
		self.x = x
		self.y = y
		
		self.outerX = 50/imgScale
		self.outerY = 50/imgScale
		self.exists = True
		
		#Picture of powerUp
		healthPUPic = "pictures/health.png"
		
		#pygame special pixel dance it likes to do with my pictures
		self.healthPU = pygame.image.load(healthPUPic).convert_alpha()
		self.healthPU = pygame.transform.scale(self.healthPU, (self.outerX,self.outerY))


	def isHit(self,player):
		#health upgrade
		player.hp += 3
		self.exists = False		
		
	def getPic(self):
		return self.healthPU
		
	def getRect(self):
		return  pygame.Rect(self.x,self.y,self.outerX,self.outerY)
