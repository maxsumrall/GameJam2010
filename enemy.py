#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 


#Things to edit: the enemies HitPoints. The enemy class and Boss class have 
#HP as a formal parameter. Edit it to change the hit points. 


import pygame,random,projectile



explodePic = "pictures/rock.png"

class Enemy(object):
	def __init__(self, x=0, y=0, vx=2, vy=2, pic ="pictures/enemyShipSmaller.png", hp=3,imgScale=1):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.hp = hp
		self.exist = True
				
		#Time for some image and graphics manipluation to scale things correctly
		# the outer bounds of the actual picture, which is the size of the picture in pixles
		scalingVar = 0.5
		self.outerX = 54/imgScale
		self.outerY = 54/imgScale
		self.shipPicture = pygame.image.load(pic).convert_alpha()
		self.explodeShip = pygame.image.load(explodePic).convert_alpha()
		self.shipPicture = pygame.transform.scale(self.shipPicture, (self.outerX,self.outerY))
		
		self.isBoss = False

	def shoot(self):
		pass
	
	def getPic(self):
		return self.shipPicture
    
	def update(self,player,projectiles):
		
		
		enemyShipSpeed = 0.3	
		
		if self.x < player.x:
			self.x += self.vx * enemyShipSpeed
		elif self.x > player.x:
			self.x += self.vx * enemyShipSpeed * -1



		if self.y > player.y:
			self.y += self.vy * enemyShipSpeed * -1
			
		elif self.y < player.y:
			self.y += self.vy * enemyShipSpeed
			
	def amIDeadYet(self):
		if(self.hp < 0):
			self.isDead()
	
	def isDead(self):
		#This is a problem, since it will flash the pic and dissapear
		self.shipPic = self.explodeShip
		self.exist = False
		
	def isHit(self):
		self.exist = False
		
	def getRect(self):
		return  pygame.Rect(self.x,self.y,self.outerX,self.outerY)
		