# Minesweeper

# Core imports
import pygame as pyg # We can now write pyg instead of pygame

# Imports of our group's code
from UI import *
from EventHandler import *


# Init game
pyg.init()

# Create a pygame display then pass it to the UI handler to set it up
gameWindow = setup_display(pyg.display)

# Surface to blit on
gameCanvas = pyg.display.set_mode((640, 480))


# Start the game

# Game loop
while True:
    # Ask the player for the game parameters
    #       Create the 'Get Parameters' window
    # Create the window based on those parameters
    draw_new_game_menu(gameCanvas)

    # Create the board (once)
    #   Draw the board on the board rectangle
    #   Other game logic stuff


    # Events
    events = pyg.event.get()
    for e in events:
        if e.type == pyg.KEYDOWN:
            # Keep a buffer of what the person is doing
            key_press(e)

        if e.type == pyg.MOUSEBUTTONDOWN:
            user_is_clicking(e)

    # Keep updating the game window
    # This is just redrawing it? Updating it? I'm not sure
    gameWindow.flip()


# End Game
#   Win or Lose?
