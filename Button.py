# The base button class
class Button:
    def __init__(self, width, height, xPos, yPos, image):
        # Dimensions
        self.width  = width
        self.height = height

        # Coordinates
        self.x = xPos
        self.y = yPos

        # Image
        self.image = image

        ''' Get Functions '''
        def get_width(self):
            return self.width

        def get_height(self):
            return self.height

        def get_x_pos(self):
            return self.x

        def get_y_pos(self):
            return self.y

        def get_image(self):
            return self.image

# Value they had for buttons ***
button_width = 80


# UI Buttons
# New Game

# Quit

# New Game buttons
new_game_button = gui_button((255,255,255), 0, 0, button_width, 40, "New Game", start_game)
new_game_button.draw(gameDisplay, 1)

# Quit button
quit_button = gui_button((255,255,255),display_width - button_width/2, 0, button_width/2, 40, "Quit", quit_game)
quit_button.draw(gameDisplay, 1)
