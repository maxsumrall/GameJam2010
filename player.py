#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 



#Things to edit here: 
#The players HitPoints. Thats a few lines down. Edit the hp default formal parameter. 

import pygame,projectile

class Player(object):
	def __init__(self, x=0, y=0, dx= 0,dy = 0,hp=130,imgScale=1):
		self.x = x
		self.y = y
		self.hp = hp
		self.dx = dx
		self.dy = dy
		self.exists = True
		#outer bounds, the size of the ship picture in pixles
		self.outerX = 183/imgScale
		self.outerY = 378/imgScale
		
		
		self.hasNuke = False
		
		#Players Ships
		userShipNormalPic = "pictures/goodShipNormal.png"
		userShipFlamesPic = "pictures/goodShipFlames.png"
		userShipLeftPic = "pictures/goodShipLeft.png"
		userShipRightPic = "pictures/goodShipRight.png"
		
		userShipNormalPicBomb = "pictures/goodShipNormalBomb.png"
		userShipFlamesPicBomb = "pictures/goodShipFlamesBomb.png"
		userShipLeftPicBomb = "pictures/goodShipLeftBomb.png"
		userShipRightPicBomb = "pictures/goodShipRightBomb.png"
		
		#Now to make the pygame special pics
		self.userShipNormal = pygame.image.load(userShipNormalPic).convert_alpha()
		self.userShipFlames = pygame.image.load(userShipFlamesPic).convert_alpha()
		self.userShipLeft = pygame.image.load(userShipLeftPic).convert_alpha()
		self.userShipRight = pygame.image.load(userShipRightPic).convert_alpha()
		
		self.userShipNormalNuke = pygame.image.load(userShipNormalPicBomb).convert_alpha()
		self.userShipFlamesNuke = pygame.image.load(userShipFlamesPicBomb).convert_alpha()
		self.userShipLeftNuke = pygame.image.load(userShipLeftPicBomb).convert_alpha()
		self.userShipRightNuke = pygame.image.load(userShipRightPicBomb).convert_alpha()
		
		
		#Now we need to scale all the pictures. This is getting messy!
		self.userShipNormal = pygame.transform.scale(self.userShipNormal, (self.outerX,self.outerY))
		self.userShipFlames = pygame.transform.scale(self.userShipFlames, (self.outerX,self.outerY))
		self.userShipLeft = pygame.transform.scale(self.userShipLeft, (self.outerX,self.outerY))
		self.userShipRight = pygame.transform.scale(self.userShipRight, (self.outerX,self.outerY))
		
		self.userShipNormalNuke = pygame.transform.scale(self.userShipNormalNuke, (self.outerX,self.outerY))
		self.userShipFlamesNuke = pygame.transform.scale(self.userShipFlamesNuke, (self.outerX,self.outerY))
		self.userShipLeftNuke = pygame.transform.scale(self.userShipLeftNuke, (self.outerX,self.outerY))
		self.userShipRightNuke = pygame.transform.scale(self.userShipRightNuke, (self.outerX,self.outerY))
		
		#Now set which ship is going to be displayed
		
		self.currentShipPicture = self.userShipNormal
		
		
	def moveShip(self, direction):
		
		movementPerKeypress = 5
		print direction
		
		up,down,left,right = 274,273,276,275
		if direction == up:
			#Moving DOWN
			self.changePic("down")		
			self.dy = movementPerKeypress
		elif direction == down:
			#Moving UP
			self.changePic("up")		
			self.dy  = -(movementPerKeypress)
		elif direction == left:
			#Moving LEFT
			self.changePic("left")
			self.dx  = -(movementPerKeypress)
		elif direction == right:
			#Moving RIGHT
			self.changePic("right")		
			self.dx = movementPerKeypress
		
		self.update()
		
	def update(self):
		self.x +=self.dx
		self.y +=self.dy
		
			
			
			
			
			
	#When an enemy ship hits the players ship
	def shipCollision(self):
		#Edit this to figure out how much damage to take
		print "hit by ship"
		self.hp = (self.hp - 2)
		
	def isHit(self):
		#Edit this to dictate how much damage to take per hit
		print "Im Hit"
		self.hp = (self.hp - 3)
		
	def outerX(self):
		return (self.x + 0) #REPLACE ZERO WITH WIDTH OF PIC
	
	def outerY(self):
		return (self.y +0) #REPLACE Y WITH THE HEIGHT OF PIC
		
	def getPic(self):
		return self.currentShipPicture
		
	def shoot(self,scale,shotCount=1, projPic ="pictures/playerLaser.png",nuke = False,):
		
		projectileSpeed = -2.5
		
		return projectile.Projectile( x = self.x, y = self.y - 100, vy = projectileSpeed,shot = shotCount,pic = projPic, nukeStatus = nuke,imgScale=scale)
	
	
	#there are different pictures for each direction its moving
	def changePic(self,direction):
		
		if(self.hasNuke):
			if direction == "up":
				self.currentShipPicture = self.userShipFlamesNuke
				
			elif direction == "left":
				self.currentShipPicture = self.userShipLeftNuke
				
			elif direction == "right":
				self.currentShipPicture = self.userShipRightNuke
				
			elif direction == "down":
				self.currentShipPicture = self.userShipNormalNuke

		else:		
			if direction == "up":
				self.currentShipPicture = self.userShipFlames
				
			elif direction == "left":
				self.currentShipPicture = self.userShipLeft
				
			elif direction == "right":
				self.currentShipPicture = self.userShipRight
				
			elif direction == "down":
				self.currentShipPicture = self.userShipNormal
				
	def isDead(self):
		self.exists = False		
	def getRect(self):
		return  pygame.Rect(self.x,self.y,self.outerX,self.outerY)
		
	def checkIfDead(self):
		if (self.hp <= 0):
			self.isDead()
			return True
		
		
	