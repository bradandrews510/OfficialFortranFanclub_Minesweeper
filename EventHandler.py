# Event handler

# Learn to import these properly!
#from pygame import pygame.event
import pygame as pyg

''' MOUSEBUTTONDOWN '''
# Case: Left click only
#       button.left_click()
def user_is_clicking(e):
    if e.button == 1:
        print("Left click")

    else:
        print("Not a left click...")

# Case: Any other click(s)
#       button.right_click()

# We can check for collisions based on rectangles or a look up table
# of some sort that keeps track of what regions belong to what buttons

''' KEYDOWN '''

# A buffer to keep track of what the user writes
# Make sure to delete it if it gets too large
usrMsg = ''

# e stands for event. We need a good naming convention
def key_press(e):
    if e.key == pyg.K_UP:
        print("Pressing up arrow")

    elif e.key == pyg.K_DOWN:
        print("Pressing the down arrow")

    elif e.key == pyg.K_LEFT:
        print("Left doesn't do anything")

    elif e.key == pyg.K_RIGHT:
        print("Right doesn't do anything")

    elif e.key == pyg.K_BACKSPACE:
        print("Backspace")

    else: # Try converting the input into an integer. If it doesn't work,
        try: # then just discard the entry and consider it invalid
            isinstance(int(e.unicode), int)
            print(e.unicode)
        except:
            print("Invalid key detected")

# Case: User entered a number
#       If we have a leading 0, ignore it
#       Otherwise, accept the input and check for validity?

# Case: User pressed 'Enter'
#       ...

# Case: User pressed 'Escape'
#       Quit the game

# Case: Arrow key
#       Navigate the row, column, and mine input fields
