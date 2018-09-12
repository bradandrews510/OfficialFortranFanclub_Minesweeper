import pygame
#from sweeper_UI import ms_buttons
#from Board.py import GameBoard

# drawing background gameboard
# start_game_input(rows, cols, mines) - rows, cols, #mines,
    #create_board()
#newgame()
    # createnew()
        #drawcells(rows, cols)
    # create number_and_mine_grid()

class new_game:
    m_rows = 0
    m_cols = 0
    m_mines = 0
    #m_board = GameBoard(rows, cols, mines)

    def __init__(self, rows, cols, mines):
        m_rows = rows
        m_cols = cols
        m_mines = mines

    def start_game(self):
        #create window, draw cells, create number and mine grid
        pygame.init()
        logo = pygame.image.load("dog.png")
        pygame.display.set_icon = logo
        pygame.display.set_caption("MINESWEEPER")

        screen = pygame.display.set_mode((800,600))

        running = True

        while running:

            image = pygame.image.load("dog.png")
            screen.blit(image, (0,0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
