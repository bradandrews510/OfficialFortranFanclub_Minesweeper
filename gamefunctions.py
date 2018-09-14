import pygame, sys, time, random
from pygame.locals import *
import random

from Board import *
from Cell import *

def recReveal(grid, rows, cols):

    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return False

    grid.board[rows][cols].set_revealed()

    if grid.board[rows][cols].get_cell_textRep()=='M':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        return True

    elif grid.board[rows][cols].get_cell_textRep()!='-':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        return False

    elif grid.board[rows][cols].get_cell_textRep()=='-':
        print(rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
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
    #print(grid.get_height(), " by ", grid.get_width())
    for rows in range(grid.get_height()):
        for cols in range(grid.get_width()):
            #print(rows, ":", cols)
            if grid.board[rows][cols].textRep=='M':
                adjacent(grid, rows-1, cols-1)
                adjacent(grid, rows-1, cols)
                adjacent(grid, rows-1, cols+1)
                adjacent(grid, rows, cols+1)
                adjacent(grid, rows+1, cols+1)
                adjacent(grid, rows+1, cols)
                adjacent(grid, rows+1, cols-1)
                adjacent(grid, rows, cols-1)

    grid.print_board()
    return

def adjacent(grid, rows, cols):
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True or grid.board[rows][cols].isMined==True:
        return

    grid.board[rows][cols].set_num_adj_mines(int(grid.board[rows][cols].numAdjacent)+1)
    grid.board[rows][cols].textRep=grid.board[rows][cols].numAdjacent
    return

#places the mines
def place_mines(grid, numofMines):
    """ @pre    The number of mines n is valid
        @post   Populates the game board with n mines
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

def game_over(gameSurface):
    print("ENTERED GAME_OVER----------")
    global FPSCLOCK, DISPLAYSURFACE  #Testing purposes
    print("TEST AREA 1----------")

    global BASICFONT, TEXTFONT, RESET_SURF, RESET_RECT, QUIT_SURF, QUIT_RECT
    print("TEST AREA 2----------")

    # pygame.init()  #Testing purposes
    # pygame.display.set_caption('Minesweeper')  #Testing purposes
    FPSCLOCK = pygame.time.Clock()  #Testing purposes
    print("TEST AREA 3----------")
    DISPLAYSURFACE = gameSurface; #Testing purposes
    print("TEST AREA 4----------")
    BASICFONT = pygame.font.SysFont('None', 30)
    print("TEST AREA 5----------")
    TEXTFONT = pygame.font.SysFont('None', 40)
    print("TEST AREA 6----------")
    RESET_SURF, RESET_RECT = drawButton('New Game', (0, 0, 0), (225, 225, 225), 200/3, 100*.75)
    print("TEST AREA 7----------")
    QUIT_SURF, QUIT_RECT = drawButton('Quit', (0, 0, 0), (225, 225, 225), 200*.75, 100*.75)
    print("TEST AREA 8----------")
    MENU_SURF = pygame.Surface((200,100))
    print("TEST AREA 9----------")
    MENU_RECT = placeSurface(MENU_SURF, DISPLAYSURFACE.get_width()/2, DISPLAYSURFACE.get_height()/2)
    print("TEST AREA 10----------")

    RESET_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)
    QUIT_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)

    mouse_x = 0
    mouse_y = 0
    running = True
    print("RUNNING = ", running, "----------")
    #DISPLAYSURFACE.fill((0,0,0))

    while(running):
        mouseClicked = False
        spacePressed = False
        running = True

        #DISPLAYSURFACE.fill((0,0,0))  #Testing purposes

        DISPLAYSURFACE.blit(MENU_SURF, MENU_RECT)
        MENU_SURF.fill((255,255,255))
        drawText("Game Over", TEXTFONT, ((0,0,0)), MENU_SURF, 200*.5, 100*.25)

        DISPLAYSURFACE.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURFACE.blit(QUIT_SURF, QUIT_RECT)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True

        if RESET_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, RESET_RECT)
            if mouseClicked:
                running = False
                pygame.quit()
                break

        # check if show box is clicked
        if QUIT_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, QUIT_RECT)
            if mouseClicked:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

def drawButton(text, textColor, backgroundColor, center_x, center_y):

    butSurf = BASICFONT.render(text, True, textColor, backgroundColor)
    buttonRect = butSurf.get_rect()
    buttonRect.centerx = center_x
    buttonRect.centery = center_y

    return (butSurf, buttonRect)

def placeSurface(screen, center_x, center_y):

    surfRect = screen.get_rect()
    surfRect.centerx = center_x
    surfRect.centery = center_y

    return surfRect

def drawText(text, font, color, surface, x, y):

    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.centerx = x
    textRect.centery = y
    surface.blit(textSurf, textRect)

def highlightButton(screen, buttonRect):

    linewidth = 4
    pygame.draw.rect(screen, (0, 128, 0), (buttonRect.left-linewidth, buttonRect.top-linewidth, buttonRect.width+2*linewidth, buttonRect.height+2*linewidth), linewidth)

print("2x2 with 2 mines")
tB = Board(5,5)
place_mines(tB,5)
board_create(tB)
tB.print_board()
recReveal(tB, 0, 0)
