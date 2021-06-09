# *****
# A class to represent the Game.
# *****

# imports
from Entity import Entity
from Board import Board
from Player import Player
from Robot import Robot
from Logger import Logger

class Game():
    # class variables
    player1: Entity
    player2: Entity
    board: Board
    turn: int
    gameover: bool

    logger = Logger()

    # initialize Game object
    def __init__(self):
        # set class variable values
        self.player1 = Player()
        self.player2 = Robot()
        self.board = Board()
        self.turn = 0
        self.gameover = False

    # method to start and run a new game
    def start(self):
        # print welcome message and info to the user
        print("\nWelcome, Player!")
        print("You will be Player 1 and are assigned the value \"X\".")
        print("\"O\" will be assigned to the computer as Player 2.")

        # print the position values for reference
        print("\nFor reference, the board spaces are numbered as follows:")
        print("row1 [  1,  2,  3,  4,  5]")
        print("row2 [  6,  7,  8,  9, 10]")
        print("row3 [ 11, 12, 13, 14, 15]")
        print("row4 [ 16, 17, 18, 19, 20]")
        print("row5 [ 21, 22, 23, 24, 25]")

        # initialize a new game board
        print("\nCreating an empty board now...")
        print("\nInitialized Board:")
        self.board.__iter__()

        # log that a new game has started to the tictactoe.txt file
        self.logger.log("\nNew Game", "tictactoe.txt")

        # while there is still an available (empty) space on the board
        # continue the game
        while(self.board.isEmptySpaceInBoard() == True):
            # if an even turn, the Player will go
            if self.turn % 2 == 0:
                # call player1 turn logic
                self.player1.onTurn(self, self.board)
                # if gameover, print message that the Player has won
                if self.gameover == True:
                    print("Congratulations Player, you have won!")
                    break
            # if an odd turn, the Robot will go
            else:
                # call player2 turn logic
                self.player2.onTurn(self, self.board)
                # if gameover, print message that the computer has won
                if self.gameover == True:
                    print("I'm sorry, the computer has won!")
                    break

        # if no spaces remain and there was no winner
        # print message to tell user there was a draw
        if self.gameover != True:
            print("Uh oh, there was a draw. Better luck next time!")