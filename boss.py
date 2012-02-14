#Written by Jonathan Sumrall
#George Mason University Game Jam 2010
#Fall 2010
#See the README for bug info and how to play. 

#Some interesting things you can edit:
#Not much actually, except you could have a blast changing the HP of the boss.
#Or maybe make the boss more immune to bombs.

import pygame,random,projectile

class Boss(object):
	def __init__(self,x=0,y=0,vx=0,vy=0,hp=100,imgScale=1):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.hp = hp
		
		#we need to create the boss image, and scale it correctly
		scalingVar = 3
		self.outerX = 500/imgScale
		self.outerY = 300/imgScale
		self.isBoss = True
		self.scale = imgScale
		bossPicture = "pictures/boss.png"
		self.exist = True
		self.BossPic = pygame.image.load(bossPicture).convert_alpha()
		self.BossPic = pygame.transform.scale(self.BossPic,
			(self.outerX, self.outerY) )
		
	def isHit(self):
		self.hp -= 2
		if self.hp < 0 :
			self.exist = False
			
			
	def getPic(self):
		return self.BossPic
		
	def getRect(self):
		return pygame.Rect(self.x,self.y,self.outerX,self.outerY)
	
	def update(self,player,projectiles):
		bossShipSpeed = 1
		
		if self.x < player.x: 
			self.vx = 1 
			
		elif self.x > player.x:
			self.vx = -1
		
		self.vx = self.vx * bossShipSpeed
		
		self.x += self.vx
		
		
		
		if (random.randint(0,100) > 99):
			projectiles.append(self.shoot(self.scale))
		
	def shoot(self,scale):
		
		projectileSpeed = 1.5
		return projectile.Projectile( x = self.x, y = self.y + self.outerY, vy = projectileSpeed, pic = "pictures/alienLaser.png",imgScale= scale)
		
	def isDead(self):
		pass
		#WE dont need this for the boss
		
	
