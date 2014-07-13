#DON'T TOUCH THE STUFF BELOW THIS LINE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pygame
import sys

white = (255,255,255)
black = (0,0,0)

pygame.init()
window = pygame.display.set_mode((600,600))
#draw the board
pygame.draw.line(window,white,(200,0),(200,600),5)
pygame.draw.line(window,white,(400,0),(400,600),5)
pygame.draw.line(window,white,(0,200),(600,200),5)
pygame.draw.line(window,white,(0,400),(600,400),5)

#display above drawings
pygame.display.flip()

#create the board array (row,col)
board = [[" " for x in range(3)] for y in range (3)]
#to access this array: board[row][col] = "X" etc.

#function used to find row and column of mouse click
def coordinates(mouse_position):
	row = int(mouse_position[0] / 200)
	col = int(mouse_position[1] / 200)
	return (row,col)

def checkBoard():
	for x in range (3):
		if board[x][0] == board[x][1] and board[x][0] == board[x][2] and board[x][0] != " ":
			return board[x][0]
		elif board[0][x] == board[1][x] and board[0][x] == board[2][x] and board[0][x] != " ":
			return board[0][x]
	if board[1][1] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
		return board[1][1]
	if board[1][1] != " " and board[2][0] == board[1][1] and board[0][2] == board[1][1]:
		return board[1][1]
	return "none"
	pass
#DON'T TOUCH THE STUFF ABOVE THIS LINE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Let's write functions to draw Xs and Os for us:
def drawX(row,column):
#Draws an X in the square where the mouse was clicked.
	#Draw your 'X' in the proper position
	#Hint: the position for the X is the top left corner of the square
	#change the board array is it knows that this row,col position is now occupied

    #Delete the "pass" below to test your code.
    pass

def drawO(row,column):
#Draws an O in the square where the mouse was clicked.
	#draw your "O" in the proper position
    #Hint: the position for the O is the center of the square
	#change the board array is it knows that this row,col position is now occupied

    #Delete the "pass" below to test your code
	pass

currentPlayer = "X"
#Main loop (remember - this loop is infinite, it runs FOREVER)
while True:
    #Default quitting condition:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
        #If the mouse is clicked
		elif event.type == pygame.MOUSEBUTTONDOWN:
            #Get the mouse position:
			position = pygame.mouse.get_pos()
            #Print out the mouse coordinates to the screen
            #These coordinates tell you which square your mouse is in
			print coordinates(position)
			#Draw the currentPlayer in the coordinates clicked
			#check the board, see if a player won or not
			winner = checkBoard()
            #If we have a winner
			if winner != "none":
				print "Player " + winner + " has won!"
                #How can we change this so a new game is started?
				sys.exit(0)
            #If we do not have a winner yet:
			else:
				pass #delete this line once you write something here!
				#Change the currentPlayer to the next player


"""
Remember!
	Switch players after every move
	you cannot play in the same place twice!
	you need to check horizontally, vertically and diagonally for a winner!
"""