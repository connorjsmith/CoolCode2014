#To make sure we have all we need for this program,
# import these guys:
import pygame
import sys

#Start pygame
pygame.init()

#Draw the pop-up window you see when you runt he program:
window = pygame.display.set_mode((500,500))

#Define some colors:
#RGB colour of white
white = (255,255,255)
#RGB color of black
black = (0,0,0)
#Try making your own colors - enter some random numbers
#between 0 and 255 to see what colour it is
random_color = (20, 150, 200)
radius = 10

#Always use an infinite loop with pygame
#Infinite loop means it runs FOREVER!
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			sys.exit(0)

    #Let's see where the mouse is at:
	position = pygame.mouse.get_pos()
	#What is in the position variable right now? Try printing it!
	#Now try drawing a circle that follows your mouse around wherever you move it!