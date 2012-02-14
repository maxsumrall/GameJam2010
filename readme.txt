Written by Jonathan Sumrall
George Mason University Game Jam 2010


This is a small arcade-type game written during George Mason University's Game Jam for Fall 2010. 
It is writeen entirely in python 2.6.6 with the pygame 1.9.1 library for some underlying window management help.

What is Game Jam? Game Jam is a torunament where teams compete to build a game in only 48 hours. 
Since this was made in only 48 hours, there are some bugs in the code:

1) No control of projectiles once left the screen. If you survive long enough (5 mintues?) the bullets will eventually loop back around and come back through the game. It's pretty interesting. 

2) I didnt scale the size of the ingame objects(ships, projectiles, etc) to the screen size. Playing on a big screen gives you plenty of room. Small screens give a much faster pace of game play. If you want to fix this, you need to do something with the bounding boxes around the objects called .outerX and .outerY in the class definitions.

3) Bombs dont seem to effect everyone the way they should. Some enemies dont get hit. Probably a problem with the bounding box.


4) probably more bugs coming.




To Play:

This game runs on python 2.6.6, and relies on the pygame 1.9 library for python 2.6.6, both are included in the folder.

Once install, you make need to edit the screen resolution for the game. Idealy this could be done with some fancy script, but you need to do it manually.

Open main.py in a text editor and edit the two value screenWidth =      and screenHeight =

set them to the right resolution for your screen.





Controls:

4 arrow keys control ship.
Space bar to shoot
"B' button shoots bomb, if you have it

When you get a "GAME OVER", switch to the terminal and hit return. This will exit the game




Objective:

Kill the alien space ships and stay alive. If you get hit with a space ship, you take damage. If you get hit by a boss's projectile, you take damage. Small ships and insta-kill, the boss takes more shots.

Bombs kill anything.