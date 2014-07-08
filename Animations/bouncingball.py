"""
Simple bouncing ball animation
"""
import pygame #used for drawing

pygame.init()#prepare pygame

window = pygame.display.set_mode((500,500))#create 500x500 window

height = 100 #start the height at 400px (500-100) height (vertical)
x = 250 #start the ball in the middle horizontally

def balldrop(height): #used to animate a dropping ball
	for y in range(height,480,1): #decrement from height to 20 (radius of circle)
		pygame.draw.circle(window,(255,255,255),(x,y),20,0)#draw a circle at x,y with radius 20
		pygame.display.flip() #display drawing
		pygame.time.wait(2)
		pygame.draw.circle(window,(0,0,0),(x,y),20,0)#erase circle

def ballrise(height):
	print "rising"
	for y in range(480,height,-1): #increment from 20 to height by 1
		pygame.draw.circle(window,(255,255,255),(x,y),20,0)
		print (x,y)
		pygame.display.flip()
		pygame.time.wait(2)
		pygame.draw.circle(window,(0,0,0),(x,y),20,0) #erase circle

while (height<480): #while the ball can keep bouncing
	balldrop(height)
	height = height+15000/(height)#multiply height by 2/3 and make sure it is an integer
	ballrise(height)#ball bounces back up


"""
Problem: the speed isn't changing as the ball rises, unrealistic.
Question: How can we make it more realistic?
"""