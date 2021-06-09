# *****
# A class to represent the robot/computer player entity.
# *****

# imports
import random

from Chess import Chess
from Entity import Entity

# sub class - inherit from Entity class
class Robot(Entity):
    # initialize Robot object
    def __init__(self):
        # call super class init method to set name
        Entity.__init__(self, "Computer")
        # call super class beToldXO method to set chess piece
        self.beToldXO(Chess.o)

    # method to define turn logic for Robot player
    def onTurn(self, game, board):
        # increment game turn
        game.turn += 1

        # choose a random position (int between 1-25)
        space = int(random.randrange(1, 26, 1))

        # get the corresponding row and col values
        row = board.rowFromPosition(space)
        col = board.colFromPosition(space)

        # if the spot is already taken continue looping
        # until a valid (empty) position is chosen
        while(board.get(row, col) != Chess.empty):
            # choose a random position (int between 1-25)
            space = int(random.randrange(1, 26, 1))

            # get the corresponding row and col values
            row = board.rowFromPosition(space)
            col = board.colFromPosition(space)

        # set the board position equal to the Robot's chess piece value
        board.set(row, col, self.chess)

        # inform the player that the computer has selected a position
        # and print the new state of the board
        print("The computer has selected position", space)
        print("The new board is as follows:")
        board.__iter__()

        # check if this move resulted in a win
        if(board.judging(self.chess) == True):
            game.gameover = True

        # log the move to the tictactoe.txt file
        self.logger.log("\n" + str(self.chess) + ":" + str(space), "tictactoe.txt")