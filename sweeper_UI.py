"""
Cell Grid, New game, help, quit buttons functionality

"""
import pygame
import sys
import math
from Board import *
from Cell import Cell
from gamefunctions import *
#import Board
#import recReveal

#cell and flag images 20x20
revealed_image = pygame.image.load("tile.png")
cell_image = pygame.image.load("cell_image.png")
flag_image = pygame.image.load("flag_tile.png")
one_image = pygame.image.load("one_tile.png")
two_image = pygame.image.load("two_tile.png")
three_image = pygame.image.load("three_tile.png")
four_image = pygame.image.load("four_tile.png")
five_image = pygame.image.load("five_tile.png")
six_image = pygame.image.load("six_tile.png")
seven_image = pygame.image.load("seven_tile.png")
eight_image = pygame.image.load("eight_tile.png")
mine_image = pygame.image.load("mine_tile.png")

cell_size = 20
cell_contents = {
    '1' : one_image,
    '2' : two_image,
    '3' : three_image,
    '4' : four_image,
    '5' : five_image,
    '6' : six_image,
    '7' : seven_image,
    '8' : eight_image,
    'M' : mine_image,
    '-' : revealed_image
}

class cell_button:
    """
    @pre cell object with draw, clicked, reveal, flag functions
    @post none
    """
    def __init__(self,x, y, width, height, cell):
        """
        @pre constructor for cell button object
        @post creates a rect at given location of given size
        """
        self.m_cell = cell
        self.rect = pygame.Rect(x * width,y * height + 40,width,height)
        self.x= x
        self.y= y
        self.size = width

class gui_button:

    def __init__(self, color, x, y, width, height, text, action = None):
        """
        @pre constructor for button object
        @post creates a rect at given location of given size
        """
        self.rect = pygame.rect.Rect(x,y,width,height)
        self.is_clicked = False
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action

    def clicked(self):
        if(self.action != None):
            self.action()

    def draw(self,window,outline="None"):
        """
        @pre draw method with option for outline
        @post button with given parameters
        @return none
        """
        if outline:
            pygame.draw.rect(window,(0,0,0),(self.x -2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))

        if self.text != "":
            font = pygame.font.SysFont(None,20)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

def quit_game():
        pygame.quit()
        quit()

def help():
    """
    @pre help function called by help button
    @post pop up message with instructions
    """
    print("Help")

"""
def reveal(row,col):
    @pre delete cell if not flagged
    @post cell is deleted, revealing grid spot
    @return None
"""

def reveal(gB, row,col):
    return recReveal(gB,row,col)



class minesweeper_gui:

        def gui_start(gB, rows, cols, mines):
                """
                start game loop
                """

                pygame.init()
                white = (255,255,255)
                black = (0,0,0)
                gray = (122,122,122)
                flags = mines
                min_width = 320
                min_height = 240

                if(cols * cell_size < min_width):
                    display_width = min_width
                else:
                    display_width = cols * cell_size
                if(rows * cell_size < min_height):
                    display_height = min_height
                else:
                    display_height = 40 + rows * cell_size

                button_width = 80
                gameDisplay = pygame.display.set_mode((display_width, display_height))
                gameDisplay.fill(black)
                pygame.display.set_caption("Minesweeper")

                cell_list = [[0 for i in range(cols)] for j in range(rows)]
                #loop through rows
                for row in range(rows):
                    #loop through each column
                    for column in range(cols):
                        #pygame.draw.rect(gameDisplay,gray, (column*cell_size, row*cell_size,cell_size,cell_size))
                        cell_list[row][column] = cell_button(column,row,cell_size,cell_size,gB.board[row][column])
                        gameDisplay.blit(cell_image, (column * cell_size, 40 + row * cell_size))

                new_game_button = gui_button((255,255,255), 0, 0, button_width, 40, "New Game", start_game)
                new_game_button.draw(gameDisplay, 1)
                #help_button = gui_button((255,255,255),0 + button_width, 0, button_width / 2, 40, "Help", help)
                #help_button.draw(gameDisplay, 1)
                quit_button = gui_button((255,255,255),display_width - button_width/2, 0, button_width/2, 40, "Quit", quit_game)
                quit_button.draw(gameDisplay, 1)
                flags_button = gui_button((255,255,255),display_width - (button_width * 2.5), 0, button_width + button_width, 40, "Flags remaining: " + str(flags))
                flags_button.draw(gameDisplay, 1)
                mine_hit = False
                while(mine_hit != True):

                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    mouse_pos = pygame.mouse.get_pos()
                                    m_rect = pygame.rect.Rect(mouse_pos, (1, 1))
                                    #on left click check for button press
                                    if(new_game_button.rect.colliderect(m_rect)):
                                        new_game_button.clicked()
                                    #elif (help_button.rect.colliderect(m_rect)):
                                        #help_button.clicked()
                                    elif (quit_button.rect.colliderect(m_rect)):
                                        quit_button.clicked()
                                    else:
                                        #check mouse collide with list of cells
                                        for row in range(rows):
                                            for cell in cell_list[row]:
                                                if (cell.rect.colliderect(m_rect)):
                                                    if cell.m_cell.isFlagged == False:
                                                        #if not flagged, turn revealed to true
                                                        print(cell.y, cell.x)
                                                        mine_hit = reveal(gB,cell.y,cell.x)


                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                                    #flag on right click
                                    mouse_pos = pygame.mouse.get_pos()
                                    m_rect = pygame.rect.Rect(mouse_pos,(1, 1))
                                    for row in range(rows):
                                        for cell in cell_list[row]:
                                            if cell.rect.colliderect(m_rect):
                                                if cell.m_cell.isRevealed != True:
                                                    if(cell.m_cell.isFlagged == True):
                                                        flags += cell.m_cell.set_flag()
                                                    else:
                                                        if(flags > 0):
                                                            flags += cell.m_cell.set_flag()
                                                    flags_button.text = "Flags remaining: " + str(flags)
                                                    flags_button.draw(gameDisplay, 1)
                    for row in range(rows):
                        for cell in cell_list[row]:
                            if cell.m_cell.isRevealed:
                                gameDisplay.blit(cell_contents[gB.board[cell.y][cell.x].get_cell_textRep()], (cell.x * cell_size, 40 + cell.y * cell_size))
                            elif cell.m_cell.isFlagged:
                                gameDisplay.blit(flag_image,(cell.x * cell_size, 40 + cell.y * cell_size))
                            else:
                                gameDisplay.blit(cell_image, (cell.x * cell_size, 40 + cell.y * cell_size))



                    pygame.display.update()
                if(mine_hit):
                    game_over(gameDisplay)
def start_game(rows,cols,mines):
    pygame.quit()
    '''
    @TODO: add input checking
    '''
    ms = minesweeper_gui
    gB = Board(cols,rows)
    place_mines(gB,mines)
    board_create(gB)
    ms.gui_start(gB,rows, cols, mines)
