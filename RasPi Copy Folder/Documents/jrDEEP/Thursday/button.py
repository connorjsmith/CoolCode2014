#Just to make sure we have all the stuff we need, import these:
#(Don't touch this code)
import pygame
import sys

#start pygame
pygame.init()

#Draw the pop up window you see when you run the program.
#Set the window dimensions:
window = pygame.display.set_mode((500,500))
#Set the window shape, color, etc.
pygame.draw.rect(window,(255,0,0),((200,200),(100,100)),0)


#Don't forget to flip!
pygame.display.flip() #display the drawings
while True:
	for event in pygame.event.get():
        #If the mouse is pressed
		if event.type == pygame.MOUSEBUTTONDOWN:
            #Store the mouse position
			pos = pygame.mouse.get_pos()
			#now check where the position actually is.
			#_if_ the mouse is inside the box and is clicked, your button should do something!
            #Hint: to see if the mouse is in the box, check whether its position
            #is within the dimensions you specified for your box.
        #Tell the program to close:
		elif event.type == pygame.QUIT:
			sys.exit(0)
