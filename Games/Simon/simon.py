import pygame
import sys
import random


redDim = (100,0,0)
greenDim = (0,100,0)
blueDim = (0,0,100)
yellowDim = (100,100,0)

redGlow = (255,0,0)
greenGlow = (0,255,0)
blueGlow = (0,0,255)
yellowGlow = (255,255,0)


window = pygame.display.set_mode((600,600))

pygame.init()
#draw the board
pygame.draw.rect(window, redDim, ((200,100),(200,100)),0)
pygame.draw.rect(window, blueDim, ((50,200),(100,200)),0)
pygame.draw.rect(window, greenDim, ((200,400),(200,100)),0)
pygame.draw.rect(window, yellowDim, ((450,200),(100,200)),0)
pygame.display.flip()


#Randomly add the next 
def addToSequence(sequence):
	number = random.randint(0,3) #generate random number between 0 and 3
	if number == 0:
		letter = "R"
	elif number == 1:
		letter = "G"
	elif number == 2:
		letter = "B"
	elif number == 3:
		letter = "Y"
	return sequence + letter


#Draw the "glowing" squares, pause for a little while, then redraw the "dim" square. ANIMATIONS!
def animateSequence(sequence, time=1000):
	for letter in sequence:
		if letter == "R":
			pygame.draw.rect(window, redGlow, ((200,100),(200,100)),0)
			pygame.display.flip()
			pygame.time.wait(time)
			pygame.draw.rect(window, redDim, ((200,100),(200,100)),0)
		#Repeat for the other colors just like above!
		elif letter == "G":
			pass
		elif letter == "B":
			pass
		elif letter == "Y":
			pass
		pygame.display.flip()
		pygame.time.wait(time/2)

sequence = addToSequence("") #start with a blank sequence
pygame.time.wait(1000)
animateSequence(sequence)
while True:
	counter = len(sequence)
	userInput = ""
	while counter > 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				#check coordinates to see if it is in range
				if pos[0] > 200 and pos [0] < 400 and pos[1] > 100 and pos[1] < 200:
					userInput += "R"
					animateSequence("R",500)
					counter += -1
				elif pos[0] > 200 and pos [0] < 400 and pos[1] > 400 and pos[1] < 500:
					userInput += "G"
					animateSequence("G",500)
					counter += -1
				elif pos[0] > 50 and pos [0] < 150 and pos[1] > 200 and pos[1] < 600:
					userInput += "B"
					animateSequence("B",500)
					counter += -1
				elif pos[0] > 450 and pos [0] < 550 and pos[1] > 200 and pos[1] < 600:
					userInput += "Y"
					animateSequence("Y",500)
					counter += -1
	if userInput == sequence:
		print "CORRECT!"
		pygame.time.wait(2000)
		#you're right! you should now start the next sequence.
		#Add to the sequence
		#Animate the sequence
	else:
		print "WRONG!!"
		pygame.time.wait(2000)
		sequence = "R"
		animateSequence(sequence)
