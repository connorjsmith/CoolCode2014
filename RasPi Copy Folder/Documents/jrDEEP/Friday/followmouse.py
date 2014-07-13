import pygame
import sys


white = (255,255,255) #create variables for the colors
black = (0,0,0)

pygame.init() #Start pygame

window = pygame.display.set_mode((500,500)) #Create a 500x500 window

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if the program is told to quit, you should close the window
			sys.exit(0)
	pos = pygame.mouse.get_pos() #finds the coordinates of the mouse
	print pos #Print out the coordinates of the mouse
	#Now do something with that position!
	#hint: Refer to simpleanimations.py