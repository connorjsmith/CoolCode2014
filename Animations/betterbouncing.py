"""
Speed varying bouncing
"""
import pygame


pygame.init()

window = pygame.display.set_mode((500,500))

velocity = 25 #starting velocity
x = 250 #horizontal position
y = 480 #vertical position

def rise(velocity):
	global y
	totalrise = 0
	for v in range(velocity,0,-1): #speed changes
		y -= v #subtract from height based on a changing speed
		totalrise += v
		pygame.draw.circle(window,(255,255,255),(x,y),20,0)
		pygame.display.flip()
		pygame.time.wait(20)
		pygame.draw.circle(window,(0,0,0),(x,y),20,0)
def fall (velocity):
	global y
	totalfall = 0
	for v in range(0,velocity+1,1): #+1 is to fix the inherit problem with range not including last number
		y += v
		totalfall += v
		pygame.draw.circle(window,(255,255,255),(x,y),20,0)
		pygame.display.flip()
		pygame.time.wait(20)
		pygame.draw.circle(window,(0,0,0),(x,y),20,0)


while (velocity > 0):
	rise(velocity)
	fall(velocity)
	velocity = int(velocity*0.75)
pygame.time.wait(2000)
