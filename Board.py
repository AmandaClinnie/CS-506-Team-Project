# *****
# A class to represent the Board.
# *****

# imports
from Chess import Chess

class Board():
    # class variables
    size = 3
    __fields = dict()

    # initialize Board object
    def __init__(self):
        # call setEmpty() method to create an empty Board
        self.setEmpty()

    # method to return Chess piece at given location
    def get(self, row, col):
        return self.__fields[row][col]

    # method to set given Chess piece at given location
    def set(self, row, col, Chess):
        self.__fields[row][col] = Chess

    # method to determine row value for given position
    def rowFromPosition(self, pos):
        if pos == 1 or pos == 2 or pos == 3:
            return "row1"
        elif pos == 4 or pos == 5 or pos == 6:
            return "row2"
        elif pos == 7 or pos == 8 or pos == 9:
            return "row3"

    # method to determine column value for given position
    def colFromPosition(self, pos):
        if pos == 1 or pos == 4 or pos == 7:
            return 0
        elif pos == 2 or pos == 5 or pos == 8:
            return 1
        elif pos == 3 or pos == 6 or pos == 9:
            return 2

    # method to iterate through the board (__fields dictionary)
    def __iter__(self):
        for key, value in self.__fields.items():
            print(key + ": [ " + value[0] + ", " + value[1] + ", " + value[2] + "]")

        # print empty line for readability
        print()

    # method to determine if there are any empty (available)
    # spaces left in the board
    def isEmptySpaceInBoard(self):
        for values in self.__fields.values():
            for value in values:
                if value.title() == Chess.empty:
                    return True

        return False

    # method to set all spaces in __fields to empty
    def setEmpty(self):
        self.__fields = {
            "row1": [Chess.empty, Chess.empty, Chess.empty],
            "row2": [Chess.empty, Chess.empty, Chess.empty],
            "row3": [Chess.empty, Chess.empty, Chess.empty]
        }

    # method to determine if there is a win
    def judging(self, chess):
        # check vertical win cases
        for i in range(0, 3):
            if self.__fields["row1"][i] == chess and self.__fields["row2"][i] == chess and self.__fields["row3"][i] == chess:
                return True

        # check horizontal win cases
        for value in self.__fields.values():
            if value[0] == chess and value[1] == chess and value[2] == chess:
                return True

        # check diagonal win cases
        if self.__fields["row1"][0] == chess and self.__fields["row2"][1] == chess and self.__fields["row3"][2] == chess:
            return True
        
        if self.__fields["row3"][0] == chess and self.__fields["row2"][1] == chess and self.__fields["row1"][2] == chess:
            return True

        # no win condition met
        return False