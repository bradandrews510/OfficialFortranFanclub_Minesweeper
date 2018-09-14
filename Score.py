''' Author: Edmundo Daniel Hidalgo
    Project 1
    Score.py

    Score.py should only save, read, and return the score data
'''


import sys
import os
import io

import csv

from Board import *


# This is the name of the save file
SCORE_SAVE_FILE = 'saves.csv'


def get_game_data(gameBoard):
# Grab this data from the game board class!
    gameData = {"width"   : gameBoard.get_width(),
                "height"  : gameBoard.get_height(),
                'mineCount'  : '5',
                'goodFlags'  : '1',
                'badFlags'   : '1',
                'win'        : True}

    return gameData


# Should we save the game so that the player can open and close their game?
#def save_game(): I'm not sure how it will handle the Cells()!
# People will also cheat!!!!


def save_score(gameBoard):
    try: # Check to see if the save file already exists
        saveFile = open(SCORE_SAVE_FILE, 'a')

        with saveFile as write_file:
            saveFields = ['width', 'height', 'mineCount', 'goodFlags', 'badFlags', 'win']
            csvWriter = csv.DictWriter(saveFile, fieldnames = saveFields)
            csvWriter.writeheader()
            csvWriter.writerow(get_game_data(gameBoard))

        saveFile.close()

    except IOError:
        print('Error' + str(IOError)) # Scary!!! I haven't test this or know how!


tB = GameBoard(2, 2, 2)
aB = GameBoard(3, 7, 4)
bB = GameBoard(4, 4, 6)
cB = GameBoard(6, 4, 1)
dB = GameBoard(4, 5, 7)
eB = GameBoard(5, 5, 3)

save_score(tB)
save_score(aB)
save_score(bB)
save_score(cB)
save_score(dB)
save_score(eB)
