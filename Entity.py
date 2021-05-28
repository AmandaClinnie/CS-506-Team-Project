# *****
# A class to represent the Entity.
# Superclass of Player and Robot.
# *****

# imports
from Chess import Chess
from Logger import Logger

class Entity():
    # class variables
    name: str
    chess: Chess

    logger = Logger()

    # initialize Entity object
    def __init__(self, name):
        # set name of Entity
        self.name = name

    # method to set chess piece of Entity
    def beToldXO(self, XO):
        self.chess = XO

    # method to obtain position from user
    def beToldPosition(self):
        # try to obtain postion
        try:
            space = int(input("Which position would you like to choose? "))

            # if an incorrent int entered, loop until valid position given
            while space > 9 or space < 1:
                print("I'm sorry, that's not a valid position. Please select a space between 1 and 9.\n")
                space = int(input("Which position would you like to choose? "))

            # return position value
            return space
        # catch ValueError - something other than int entered
        except ValueError:
            # print error message and return 0
            print("I'm sorry, that's not a valid position. Please select a space between 1 and 9.\n")
            return 0

    # method to define turn logic for human player
    def onTurn(self, game, board):
        # increment game turn
        game.turn += 1

        # initialize space variable to 0
        space = 0

        # loop until a valid position (1-9) is given
        # obtained by beToldPosition() method
        while space > 9 or space < 1:
            space = self.beToldPosition()

        # get the corresponding row and col values
        row = board.rowFromPosition(space)
        col = board.colFromPosition(space)

        # if the spot is already taken continue looping
        # until a valid (empty) position is chosen
        while(board.get(row, col) != Chess.empty):
            # print error message
            print("I'm sorry, that space is taken. Please select a new position.\n")

            # re-initialize space variable to 0
            space = 0

            # loop until a valid position (1-9) is given
            # obtained by beToldPosition() method
            while space > 9 or space < 1:
                space = self.beToldPosition()

            # get the corresponding row and col values
            row = board.rowFromPosition(space)
            col = board.colFromPosition(space)

        # set the board position equal to the Player's chess piece value
        board.set(row, col, self.chess)

        # print the new state of the board
        print("The new board is as follows:")
        board.__iter__()

        # check if this move resulted in a win
        if(board.judging(self.chess) == True):
            game.gameover = True

        # log the move to the tictactoe.txt file
        self.logger.log("\n" + str(self.chess) + ":" + str(space), "tictactoe.txt")