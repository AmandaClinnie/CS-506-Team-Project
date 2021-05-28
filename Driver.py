# *****
# A class to drive the game.
# *****

# imports
from Game import Game

# get input to see if the user wants to play
print("Hello, user! Would you like to play a game of tic tac toe?")
play = input("Enter y or n: ")

# if y, create a Game object and start the game
if play == 'y':
    game = Game()
    game.start()
# if n, quit the program
elif play == 'n':
    print("Oh, okay. Maybe next time!")
# if incorrect input, quit the program
else:
    print("That wasn't an option... I guess you don't want to play. See you next time!")