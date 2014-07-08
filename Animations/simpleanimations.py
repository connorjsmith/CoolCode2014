"""
jrDEEP Example Code
Activity: Simple Animations
"""

import pygame #used for drawing and displaying the Animations
import sys #used to handle exit calls

pygame.init() #initialize pygame, tell it were going to start drawing soon
window = pygame.display.set_mode((500,500)) #create a 500x500px window

y = 250 #start the figure at 250px in the y direction
for x in range (50,200,1): #Count from 50 -> 200 by 1s
	
	pygame.draw.circle(window,(255,255,255),(x,y),50,0)#Draw a white circle to the window which is filled
	pygame.display.flip()#display all the drawing
	pygame.time.wait(10)#wait 10ms
	pygame.draw.circle(window,(0,0,0),(x,y),50,0)

pygame.time.wait(1000)	#Pauses before exiting

"""
time for whole animation:
	counting from 50 to 200: 150 "counts"
	10ms per "count"
	150*10ms = 1500ms = 1.5s
"""
		