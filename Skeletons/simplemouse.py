import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500,500))

white = (255,255,255)#RGB colour of white
black = (0,0,0)
radius = 10

while True: #always use an infinite loop with pygame
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			sys.exit(0)
	position = pygame.mouse.get_pos()
	#What is in the position variable right now? Try printing it!
	#Now try drawing a circle that follows your mouse around wherever you move it!