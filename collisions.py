#Written by Jonathan Sumrall
#George Mason University Game Jam 2010

#See the README for bug info and how to play. 

#objects list taken as parameter, and a list of projectiles
def detectCollisions(shipObjects,projectiles,powerUps,nuke,playerShip,screen):

	#Check to make sure that each ship is not in contact with any projectile
	hitEnemies= 0
	thereIsABomb = False
	for bomb in nuke:
		powerUps.append(bomb)
		thereIsABomb = True
	#To be lazy, I'm going to add the players ship to the list of enemy ships to detect for collisions
	shipObjects.append(playerShip)
	for upgrade in powerUps:		
		if ( playerShip.getRect().colliderect(upgrade.getRect() ) ):
			upgrade.isHit(playerShip)



	for ship in shipObjects:
		for bullet in projectiles:
			if (  ship.getRect().colliderect(bullet.getRect() )  ):
				if bullet.isNuke:
					bullet.nukeExplode(shipObjects,ship,screen)
					
				bullet.hitShip()
				ship.isHit()
				hitEnemies += 1
				
	
		#Once I check for bullet hits, then you want to check for ship-ship collisions
		
		#The way I check ship-ship is to see if either X coord and either Y coord is within the X or Y coord of the players ship.
		
		#check to make sure that we're not dealing with the same players ship. playerShip is also in the ship list.
		if(playerShip != ship):
			if (  ship.getRect().colliderect(playerShip.getRect() )   ):
				playerShip.shipCollision()
				ship.isDead()
		

		
	#When we're all done here, remove the player ship from the list (Undo what we jusrt did at the top of the file)
	#.pop() removes the last item by default
	shipObjects.pop()
	
	if thereIsABomb:
		powerUps.pop()
	
	return hitEnemies
