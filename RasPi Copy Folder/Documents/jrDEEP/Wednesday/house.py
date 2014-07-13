"""
Name: Connor Smith
Date:
Description:
"""

import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

#base of house
pygame.draw.line(window,(255,255,255),(100,500),(100,300),3)
pygame.draw.line(window,(255,255,255),(300,500),(300,300),3)
pygame.draw.line(window,(255,255,255),(100,300),(300,300),3)
#~~~~~~~~~~~~~Draw fill
#roof
pygame.draw.line(window,(255,255,255),(100,300),(200,200),3)
pygame.draw.line(window,(255,255,255),(300,300),(200,200),3)
pygame.draw.circle(window,(255,255,255),(200,265),25,3)
pygame.draw.line(window,(255,255,255),(200,240),(200,290),3)
pygame.draw.line(window,(255,255,255),(175,265),(225,265),3)

#window
pygame.draw.rect(window,(255,255,255),((125,350),(50,50)),3)
pygame.draw.line(window,(255,255,255),(125,375),(175,375),3)
pygame.draw.line(window,(255,255,255),(150,350),(150,400),3)

#front door
pygame.draw.line(window,(255,255,255),(225,500),(225,400),3)
pygame.draw.line(window,(255,255,255),(275,500),(275,400),3)



pygame.display.flip() #display drawings

pygame.time.wait(5000)