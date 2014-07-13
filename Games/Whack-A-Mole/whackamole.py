import pygame
import sys
import random
import time


white = (255,255,255) #define the colours
black = (0,0,0)
red = (255,0,0)

window = pygame.display.set_mode((800,800))
pygame.init()
#draw mole holes
for y in range(100,750,150): #count by 150s from 100 to 750 (4 rows)
	for x in range (100,750,150): #count by 150s from 100 to 750 (4 rows)
		pygame.draw.circle(window, white, (x,y),70,3)

pygame.display.flip()

def coordinates(pos):
	row = int((pos[1]-30) / 150)
	col = int((pos[0]-30) / 150)
	if row < 0:
		row = 0
	if col < 0:
		col = 0
	if col > 4:
		col = 4
	if row > 4:
		row = 4
	return (row,col)

def drawMole(position):
	x = position[1]*150 + 100
	y = position[0]*150 + 100
	pygame.draw.circle (window,red,(x,y),67,0)
	pygame.display.flip()

def eraseMole(position):
	#Should be very similar to the drawMole function, except it should erase a mole instead of drawing it
	pass

def randomMoles():
	#randomly select 3 positions, store in array
	while len(moles) < 3:
		row = random.randint(0,4) 
		col = random.randint(0,4)
		if not((row,col) in moles): #prevents duplicate moles (2 moles in the same hole = IMPOSSIBLE)
			moles.append((row,col))
	for mole in moles: #for every randomly created mole in the moles array
		drawMole(mole)
		



moles = []

hits = 0 #start the game with 0 hits and 0 misses
misses = 0


pygame.time.wait(1000)
randomMoles() #create random moles
startTime = time.time() #used to time the game
currentTime = time.time()
while currentTime - startTime < 30: #30 second timer
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if you tell the window to close
			sys.exit(0) #turn off the program
		
		elif event.type == pygame.MOUSEBUTTONDOWN: #if it detects a click
			pos = pygame.mouse.get_pos() #get the position of the click
			coords = coordinates(pos) #change the click into what-a-mole coordinates
		
			if coords in moles: #if the clicked position is in the moles array
				print "You whacked one!"
				#You need to _erase_ the clicked mole
				
				#remove the clicked mole from the array
				moles.remove(coords) 
				
				#add 1 to hits

				if len(moles) == 0: #if there are no more moles left
					pygame.time.wait(500)
					#what should you do when you run out of moles to whack?
			else: 
				print "MISS!"
				#add 1 to misses
	currentTime = time.time()

print "TIME UP!"
#Print how many hits, misses and the percentage of hits the player made!