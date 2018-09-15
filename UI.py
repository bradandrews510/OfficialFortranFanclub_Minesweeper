"""
Cell Grid, New game, help, quit buttons functionality
"""

import pygame as pyg # Careful with circular dependencies! This may not
# even be necessary, I haven't checked or thought about it but we need to

# Our imports
from Board import *
from Cell import Cell
from AssetManager import *

from Button import Button

# Parameters: Image, screen?
# Add error checking


# New Game Window
#       [Label Enter # of rows:    ] [Input Field]
#       [Label Enter # of columns: ] [Input Field]
#       [Label Enter # of mines:   ] [Input Field]
#       Button: OK

# Game Window
#   Button: New Game    Button: Quit    Flags Remaining: XXX
#   ********************************
#   *         Game Board           *
#   *         Game Board           *
#   *         Game Board           *
#   *         Game Board           *
#   *         Game Board           *
#   *         Game Board           *
#   ********************************

# Init the font stuff
try:
    pyg.font.init()
    # Courier is a common but NOT universally available font
    coreFont = pyg.font.SysFont("courier", 18)
except:
    print("Error loading font")


''' Daniel G '''
def setup_display(pygDisplay):
    # Window geometry - Values are hardcoded at the moment
    pygDisplay.set_mode((640, 480))
    # Disable resizing

    # Captions, icons, and logos
    pygDisplay.set_caption("Minesweeper - Official Fortran Fanclub")

    # Get images from the Asset Manager and then use them here
    #logo = pygame.image.load("mine_tile.png")
    #pygame.display.set_icon(logo)

    return pygDisplay

# I think instead it would be better to have a 'draw UI' function that pulls
# the UI's layout from a file instead of 'draw_new_game_menu', 'draw_playfield',
# 'draw_whatever', but for the sake of time this will have to do
''' Daniel G '''
def draw_new_game_menu(pygCanvas):
    # A canvas where all the labels will be drawn

    # Label: Enter rows
    draw_label("Enter the number of rows: ", coreFont, WHITE, pygCanvas, 0, 0)
    # Text entry for row input

    # Label: Enter columns
    draw_label("Enter the number of columns : ", coreFont, WHITE, pygCanvas, 0, 25)
    # Text entry for column input

    # Label: Enter mines
    # Text entry for column input

    # Create buttons and text entry stuff
    pygCanvas.blit(butNewGame, (0, 400)) # Hardcoded position
    pygCanvas.blit(butQuit,  (560, 400)) # Hardcoded position



''' Sydney
#def draw_minesweer_board(pygCanvas):
    # Draw the menu somewhere in the top of the canvas
    # The only part of the menu that will change regularly is the
    # 'Flags Remaining' counter, so the 'New Game' and whatever else don't need
    # to be redrawn or updated anymore

    # The bulk majority of the canvas is likely going to be dedicated to the
    # board itself, but that's not always true. When we have a small number of
    # cells we will have empty space in the background, so keep that in mind

    # Draw the gameboard

    # Create animate board of pink tiles
    image = pygame.image.load("tile.png")
    for x in range(self.m_rows):
        for y in range(self.m_cols):
            screen.blit(image, (x*20,y*20))
'''

# We can get rid of the font parameter if we don't care about using different
# fonts or font sizes. Currently it doesn't even do anything since we just
# pass coreFont which is globally accessible in UI.py anyway
def draw_label(text, font, color, pygCanvas, xPos, yPos):
    # Create a Pygame Surface object with the passed text and color
    # The 1 in the parameter has to do with the level of anti-aliasing
    label = coreFont.render(text, 1, color)

    # Draw the above Pygame Surface onto the canvas that got passed
    pygCanvas.blit(label, (xPos, yPos))

# Will we be using image based buttons? If so, just draw them like any other
# image and attach a hitbox (rect object) to them. There's no need for them to
# have an entire function dedicated to them unless they _NEED_ to operate
# differently than the other interactable components
#def draw_button()
