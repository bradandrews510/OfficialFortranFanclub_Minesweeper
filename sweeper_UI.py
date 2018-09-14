"""
Cell Grid, New game, help, quit buttons functionality

"""
import pygame
import sys
#import recReveal
cell_image = pygame.image.load('cell_image.png')
flag_image = pygame.image.load('cell_flag.png')
'''
def button(msg, x_pos, y_pos, width, height, color, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        self.font = pygame.font.Sysfont("Arial",20)
        gameDisplay.blit(self.font.render(msg, True, (0,0,0)
        if x_pos+width > mouse[0] > x_pos and y_pos+height > mouse[1] > y_pos:
                if(click[0] == 1 and action != None):
                        action()


        gameDisplay.update()
'''
class cell_button:

    def __init__(self, x, y, size, img = cell_image):
        self.x_pos = x
        self.y_pos = y
        self.size = size
        self.img = img

    def clicked():
        if pygame.mouse.get_pressed[0] == 1:
            self.reveal
        if pygame.mouse.get_pressed[2] == 1:
            self.flag

    def reveal():
        self.is_revealed = True

    def flag():
        self.is_flagged = True
        self.img = flag_image



class gui_button:

    def __init__(self, color, x, y, width, height, text, action = None):
        '''
        constructor
        '''
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

    def draw(self,win,outline="None"):
        '''
        draw method with option for outline
        '''
        if outline:
            pygame.draw.rect(win,(0,0,0),(self.x -2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

        if self.text != '':
            font = pygame.font.SysFont(None,20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        '''
        determine if mouse is over button
        '''
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def quit_game():
        pygame.quit()
        quit()

def new_game():
    print("New Game")

def help():
    print("Help")

def num_flags(inc):
    flags_button.text = "Flags remaining: " + str(mines)
"""
def reveal():
        col = display_width/x_pos
        row = (display_height - 40)/y_pos
        reveal(row, col)
"""

class minesweeper_gui:

        def gui_start(rows,cols,mines):
                """
                start game loop
                """

                pygame.init()
                white = (255,255,255)
                black = (0,0,0)
                gray = (122,122,122)
                cell_size = 20
                min_width = 320
                min_height = 220

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

                #loop through rows
                for row in range(rows):
                        #loop through each column
                        for column in range(cols):
                                #draw resource at position
                                #pygame.draw.rect(gameDisplay,gray, (column*cell_size, row*cell_size,cell_size,cell_size))
                                gameDisplay.blit(cell_image, (column * cell_size, 40 + row * cell_size))


                pygame.display.set_caption('Minesweeper')
                running = True
                new_game_button = gui_button((255,255,255), 0, 0, button_width, 40, "New Game", new_game)
                new_game_button.draw(gameDisplay, 1)
                help_button = gui_button((255,255,255),0 + button_width, 0, button_width / 2, 40, "Help", help)
                help_button.draw(gameDisplay, 1)
                quit_button = gui_button((255,255,255),display_width - button_width/2, 0, button_width/2, 40, "Quit", quit_game)
                quit_button.draw(gameDisplay, 1)
                flags_button = gui_button((255,255,255),display_width - (button_width * 2.5), 0, button_width + button_width, 40, "Flags remaining: " + str(mines))
                flags_button.draw(gameDisplay, 1)
                while(running):

                    #button("Quit", display_width - 50, 0, 5, 40, (white), quit_game)
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    running = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = pygame.mouse.get_pos()
                                    m_x = mouse_pos[0]
                                    m_y = mouse_pos[1]
                                    print(event)
                                    if(m_x <= button_width and m_y <= 40):
                                        new_game_button.clicked()
                                    elif (m_x <= button_width * 2 and m_y <= 40):
                                        help_button.clicked()
                                    elif (m_x >= display_width - button_width and m_y <= 40):
                                        quit_button.clicked()
                                    else:
                                        pass
                    pygame.display.update()

#display_width = 800
#display_height = 600
#gameDisplay = pygame.display.set_mode((display_width, display_height))
#ms = minesweeper_gui()
#ms.gui_start(10,10,0)
