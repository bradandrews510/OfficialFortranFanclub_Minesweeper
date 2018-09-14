import pygame
from sweeper_UI import ms_buttons
#from Board import GameBoard

# drawing background gameboard
# initialization and start game
# detect mouse clicks, update graphics based on revealed board

class new_game:
    m_rows = 0
    m_cols = 0
    m_mines = 0
    #m_board = GameBoard(rows, cols, mines)

    def __init__(self, rows, cols, mines):
        self.m_rows = rows
        self.m_cols = cols
        self.m_mines = mines

    def start_game(self):
        #create window, draw cells, create number and mine grid
        pygame.init()
        logo = pygame.image.load("dog.png")
        pygame.display.set_icon = logo
        pygame.display.set_caption("MINESWEEPER")

        n = self.m_rows * 20
        m = self.m_cols * 20
        screen = pygame.display.set_mode((n,m))

        background = pygame.Surface(screen.get_size())
        background.fill((255,255,255))
        background = background.convert()
        screen.blit(background, (0,0))

        image = pygame.image.load("tile.png")
        for x in range(self.m_rows):
            for y in range(self.m_cols):
                screen.blit(image, (x*20,y*20))
                pygame.display.flip()

        self.run_game();

    def run_game(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
