import pygame
import sys


pygame.init()

window = pygame.display.set_mode((500,500))

pygame.draw.rect(window,(255,0,0),((200,200),(100,100)),0)

pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type = pygame.MOUSEDOWN: #mouse is clicked
			position = pygame.mouse.get_pos() #store the mouse position
			#now check where the position is.
			#if the mouse is inside the box and is clicked, your button should do something!
