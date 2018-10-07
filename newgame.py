import pygame
#from Board import GameBoard

# drawing background gameboard
# initialization and start game
# detect mouse clicks, update graphics based on revealed board

class new_game:

    def __init__(self, rows, cols, mines):
        print("FUCKL FUCK FUCK")
        self.m_rows = rows
        self.m_cols = cols
        self.m_mines = mines
        #self.m_board = GameBoard(self.m_cols, self.m_rows, self.m_mines)

    def start_game(self):
        #create window, draw cells, create number and mine grid
        pygame.init()
        logo = pygame.image.load("mine_tile.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("MINESWEEPER")

        # n: number of pixels down
        # m: number of pixels across
        # gives you an nxm window
        n = self.m_rows * 20
        m = self.m_cols * 20
        screen = pygame.display.set_mode((n,m))

        # Create background surface, fill with white color
        background = pygame.Surface(screen.get_size())
        background.fill((255,255,255))
        background = background.convert()
        screen.blit(background, (0,0))

        # Create animate board of pink tiles
        image = pygame.image.load("tile.png")
        for x in range(self.m_rows):
            for y in range(self.m_cols):
                screen.blit(image, (x*20,y*20))
        pygame.display.flip()

    def run_game(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
