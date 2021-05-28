# *****
# A class to represent the human player entity.
# *****

# imports
from Entity import Entity
from Chess import Chess

# sub class - inherit from Entity class
class Player(Entity):
    # initialize Player object
    def __init__(self):
        # call super class init method to set name
        Entity.__init__(self, "Player")
        # call super class beToldXO method to set chess piece
        self.beToldXO(Chess.x)