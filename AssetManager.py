# Asset Manager

import os

# I'm not sure how to handle imports better... or if it's even possible
import pygame

# This is currently only set up for PyGame images
def load_asset(assetPath):
    path = os.getcwd() + '/Resources/'

    try:
        asset = pygame.image.load(path + assetPath)
        return asset
    except:
        print('Error. Take a guess')


''' We're loading all of our images here
    Since we plan on reusing these images so often, I'm just gonna load
    them all up at the start and keep them in memory
'''
# Reference tilesNum[n] to get the tile_n image
tilesNum = ['tile_0.png',
            'tile_1.png',
            'tile_2.png',
            'tile_3.png',
            'tile_4.png',
            'tile_5.png',
            'tile_6.png',
            'tile_7.png',
            'tile_8.png']

for t in range(0, len(tilesNum)):
    tilesNum[t] = load_asset(tilesNum[t])


#tileRevealed = pygame.image.load("tile.png") I'm not sure what this should be
tileCell = load_asset('tile_cell.png')
tileFlag = load_asset('tile_flag.png')
tileMine = load_asset('tile_mine.png')

# Button images
butNewGame = load_asset('button_NewGame.png')
butQuit    = load_asset('button_Quit.png')


''' Color constants '''
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GRAY  = (122, 122, 122)
