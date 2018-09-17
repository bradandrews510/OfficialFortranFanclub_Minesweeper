"""@package docstring
   Game Board... this file or the class needs to be renamed
"""
import pygame, sys, time, random
from pygame.locals import *
import random

from Board import *
from Cell import *

def recReveal(grid, rows, cols):
    """ @pre    Grid is a valid object of type Board, rows and cols is the location in the board to reveal
        @post   will reveal all
        @return returns true if the cell in question is a mine, false if it is not
    """
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return False

    grid.board[rows][cols].set_revealed()

    if grid.board[rows][cols].get_cell_textRep()=='M':
        return True

    elif grid.board[rows][cols].get_cell_textRep()!='-':
        return False

    elif grid.board[rows][cols].get_cell_textRep()=='-':
        recReveal(grid, rows-1, cols-1)
        recReveal(grid, rows-1, cols)
        recReveal(grid, rows-1, cols+1)
        recReveal(grid, rows, cols+1)
        recReveal(grid, rows+1, cols+1)
        recReveal(grid, rows+1, cols)
        recReveal(grid, rows+1, cols-1)
        recReveal(grid, rows, cols-1)


    return False

def board_create(grid):
    """ @pre    grid is of type Board
        @post   Populates the board with numbers of adjacent mines for each cell.
        @return None
    """
    for rows in range(grid.get_height()):
        for cols in range(grid.get_width()):
            if grid.board[rows][cols].textRep=='M':
                adjacent(grid, rows-1, cols-1)
                adjacent(grid, rows-1, cols)
                adjacent(grid, rows-1, cols+1)
                adjacent(grid, rows, cols+1)
                adjacent(grid, rows+1, cols+1)
                adjacent(grid, rows+1, cols)
                adjacent(grid, rows+1, cols-1)
                adjacent(grid, rows, cols-1)
    return

def adjacent(grid, rows, cols):
    """ @pre    grid is of type board
        @post   Increments the numAdjacent of the cell in question by one if it is in the bounds of the board. Also changes the textRep to be the new numAdjacent.
        @return None
    """
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True or grid.board[rows][cols].isMined==True:
        return

    grid.board[rows][cols].set_num_adj_mines(int(grid.board[rows][cols].numAdjacent)+1)
    grid.board[rows][cols].textRep=grid.board[rows][cols].numAdjacent
    return

#places the mines
def place_mines(grid, numofMines):
    """ @pre    grid is of type Board, The number of mines n is valid
        @post   Populates the game board with n mines placed randomly
        @return None
    """
    #print("In place_mines")

    mCounter = numofMines
    while mCounter > 0:
        i = random.randint(0, grid.height - 1)
        j = random.randint(0, grid.width  - 1)

        if grid.board[i][j].isMined == False:
            grid.board[i][j].set_mine()
            mCounter = mCounter - 1
    return

def game_over(gameSurface):
    """ @pre    gameSurface is the main display for pygame
        @post   opens a game over screen with a quit button to quit pygame
        @return None
    """
    global BUTTONFONT, TEXTFONT, BUTTONCOLOR, BLACK, WHITE

    BUTTONFONT = pygame.font.SysFont('None', 40)
    TEXTFONT = pygame.font.SysFont('None', 40)
    BUTTONCOLOR = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    QUIT_SURF, QUIT_RECT = create_button('Quit', 200*.5, 100*.75)
    MENU_SURF = pygame.Surface((200,100))
    MENU_RECT = place_surface(MENU_SURF, gameSurface.get_width()/2, gameSurface.get_height()/2)

    QUIT_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)

    mouse_x = 0
    mouse_y = 0
    running = True

    while(running):
        mouseClicked = False
        spacePressed = False
        running = True

        gameSurface.blit(MENU_SURF, MENU_RECT)
        MENU_SURF.fill(WHITE)
        create_text("Game Over", MENU_SURF, 200*.5, 100*.25)

        gameSurface.blit(QUIT_SURF, QUIT_RECT)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True

        if QUIT_RECT.collidepoint(mouse_x, mouse_y):
            if mouseClicked:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def create_button(text, x, y):
    """ @pre    none
        @post   Creates a surface and text with different color for the background and text, along with a rectangle at that location
        @return the surface and rectangle created called buttonSurf, buttonRect
    """
    buttonSurf = BUTTONFONT.render(text, True, BLACK, BUTTONCOLOR)
    buttonRect = buttonSurf.get_rect()
    buttonRect.centerx, buttonRect.centery = x, y

    return (buttonSurf, buttonRect)

def place_surface(screen, x, y):
    """ @pre    none
        @post   returns a rectangle for the given surface that is moved to the given position
        @return the rectangle for the surface, surfRect
    """
    surfRect = screen.get_rect()
    surfRect.centerx, surfRect.centery = x, y

    return surfRect

def create_text(text, surface, x, y):
    """ @pre    none
        @post   creates text centered at the x and y position given relative to the surface and blits it on
        @return None
    """
    textSurf = TEXTFONT.render(text, True, BLACK)
    textRect = textSurf.get_rect()
    textRect.centerx ,textRect.centery = x, y
    surface.blit(textSurf, textRect)
