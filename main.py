#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 

#Some interesting things you can edit:
#Screen size - those vairbales are set a few lines below here

#In createBasicEnemies() and createPowerUps() have random function calls
#to determine how often to spawn enemies and such. Edit those for more or less enemies


import pygame, sys, time, random
from math import *
from pygame.locals import *

import collisions, player,enemy,upgrades,boss,nuke

#Load the pictures to use
bif = "pictures/bigbg.jpg"
gameOverPic = "pictures/gameOver.jpg"


pygame.init()

#Create the window
screenWidth = 1200	
screenHeight = 700

#Im going to define and figure out how to scale each element of the game
#such as the ships and enemies based on the size of the screen

scale = (screenWidth/screenHeight)*2


screen = pygame.display.set_mode((screenWidth,screenHeight),0,32)
                                                                  
#Do some pygame maintainance with the pics, making them good to use
background = pygame.image.load(bif).convert()
gameOver = pygame.image.load(gameOverPic).convert()

background = pygame.transform.scale(background, (screenWidth, screenHeight))
gameOver = pygame.transform.scale(gameOver, (screenWidth, screenHeight))


#Master lists of objects: Ships, and projectiles
shipsInPlay = []
projectiles = []
powerUps = []
nukeInPlay = [] #idk why im making this a list. im in a hurry


#Number of enemies hit. This concept is that once you shoot so many enemies, the boss appears.
numberOfEnemiesHit = 0

#jsut throwing this in here to only make 1 boss
bossNotExist = True


score = 0

#Create the USER CONTROLLED PLAYER
player = player.Player(imgScale = scale)

#Give the player's ship an initial coordinate position and velocity:

player.x = (screenWidth/2)
player.y = (screenHeight-300)

def createPowerUps():
	#Power ups work just like enemies
	if len(powerUps) < 2 :
		if random.randint(0,1000) > 998:
			powerUps.append(upgrades.HealthPowerUp(x = random.randint(0, screenWidth), y = random.randint(0,screenHeight),imgScale=scale ) )
			
	if (len(nukeInPlay) == 0) and ( not player.hasNuke ) :
		if random.randint(0,1000) > 998 :
			nukeInPlay.append(nuke.Nuke(x = random.randint(0, screenWidth), y = random.randint(0,screenHeight),imgScale=scale ) )
			
			


def createBasicEnemies():
	#There should always be atleast 1 enemy on the screen
	if len(shipsInPlay) == 0:
		shipsInPlay.append(enemy.Enemy(x = random.randint(0, screenWidth ),imgScale=scale))	
		
	#make more enemies appear randomly

	elif random.randint(0,100) > 98:
		shipsInPlay.append(enemy.Enemy(x = random.randint(0, screenWidth ),imgScale=scale ) )
		
		
def createBoss():
	shipsInPlay.append(boss.Boss(x = screenWidth/2, vx = 3,imgScale=scale) )
		
def drawHealthBar():
	pygame.draw.rect(screen,(255, 0, 0), (50,  50,   (player.hp * 10),   10) ) 
	
def checkIfPlayerDied():
	if (player.checkIfDead() ):		
		screen.blit(gameOver, (0,0) )
			
	else:
		screen.blit(background, (0,0) )

		
#This is the continious loop I was told games are supposed to have
while player.exists:
	
	#Pygame creates nice events to use. 
	#Of course, we need to let the game quit when we need it click quit
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#But, here's the important stuff. When the player does something...
		elif event.type == KEYDOWN:
			
			if event.key in (K_DOWN,K_UP,K_LEFT,K_RIGHT):
				player.moveShip(event.key)
			
			elif event.key == K_SPACE:
				#we're going to make a new projectile and append it to the list of projectiles
				#pass in the picture of the projectile to .shoot()
				if not bossNotExist:
					for ship in shipsInPlay:
						if ship.isBoss:
							projectiles.append(ship.shoot(scale))
							if not ship.exist:
								numberOfEnemiesHit = 0 
						
				
				projectiles.append( player.shoot(scale,shotCount = 1) )
				projectiles.append( player.shoot(scale,shotCount = 2) )


			elif event.key == K_b:
				if player.hasNuke:
					projectiles.append( player.shoot(scale,projPic = "pictures/theBomb.png", nuke = True) )
					player.hasNuke = False
				
			
				
		elif event.type == KEYUP:
			player.dx,player.dy = 0,0
			player.changePic("down")
	
	
	
	#Create some enemies on the screen, psudo random
	#Once you shoot so many, enemies, you make the boss!
	if numberOfEnemiesHit < 25:
		createBasicEnemies()
		
	elif bossNotExist:
		createBoss()
		bossNotExist = False	
		
	createPowerUps()
		
	#check for collisions between ship vs ships and ships vs bullets
	numberOfEnemiesHit += collisions.detectCollisions(shipsInPlay, projectiles,powerUps,nukeInPlay,player,screen)			
				
	checkIfPlayerDied()

	#Update the images on the screen. BLIT does each image, and I guess you need to do an .update() to finish it all off
	#Make sure you do the background first, then each smaller pic like the ships.

 	###########background blit is done in the previous Function call########	
	
	#update the players position	
	player.update()
	screen.blit(player.getPic(),(player.x,player.y) )
	
	drawHealthBar()

	for upgrade in powerUps:
		if upgrade.exists:
			screen.blit(upgrade.getPic(), (upgrade.x,upgrade.y) )
		else:
			powerUps.remove(upgrade)
			
	for ship in shipsInPlay:
		ship.update(player,projectiles)
		if ship.exist:
			screen.blit(ship.getPic(), (ship.x, ship.y) )
		else:
			if ship.isBoss:
				numberOfEnemiesHit = 0
				bossNotExist = True
				
			#Ship must not exists I guess
			shipsInPlay.remove(ship)
	
	for bullet in projectiles:
		bullet.update(screenHeight)
		if bullet.exist:
			screen.blit(bullet.getPic(), (bullet.x,bullet.y) )
		else:
			projectiles.remove(bullet)
			
	for bomb in nukeInPlay:
		if bomb.exist:
			screen.blit(bomb.getPic(), (bomb.x, bomb.y) )
		
		else:
			nukeInPlay.remove(bomb)
		

	#Now the everything is set up right, update the screen for the player to see
	pygame.display.update()
	
	

	
#After the player dies and the game ends, the main loops ends.
#This should hold the screen.
raw_input("GAME OVER. PRESS ENTER")







