# *****
# A class to represent the Board.
# *****

# imports
from Chess import Chess

class Board():
    # class variables
    size = 5
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
        if pos > 0 and pos < 6:
            return "row1"
        elif pos > 5 and pos < 11:
            return "row2"
        elif pos > 10 and pos < 16:
            return "row3"
        elif pos > 15 and pos < 21:
            return "row4"
        elif pos > 20 and pos < 26:
            return "row5"

    # method to determine column value for given position
    def colFromPosition(self, pos):
        if pos == 1 or pos == 6 or pos == 11 or pos == 16 or pos == 21:
            return 0
        elif pos == 2 or pos == 7 or pos == 12 or pos == 17 or pos == 22:
            return 1
        elif pos == 3 or pos == 8 or pos == 13 or pos == 18 or pos == 23:
            return 2
        elif pos == 4 or pos == 9 or pos == 14 or pos == 19 or pos == 24:
            return 3
        elif pos == 5 or pos == 10 or pos == 15 or pos == 20 or pos == 25:
            return 4

    # method to iterate through the board (__fields dictionary)
    def __iter__(self):
        for key, value in self.__fields.items():
            print(key + ": [ " + value[0] + ", " + value[1] + ", " + value[2] + ", " + value[3] + ", " + value[4] + "]")

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
            "row1": [Chess.empty, Chess.empty, Chess.empty, Chess.empty, Chess.empty],
            "row2": [Chess.empty, Chess.empty, Chess.empty, Chess.empty, Chess.empty],
            "row3": [Chess.empty, Chess.empty, Chess.empty, Chess.empty, Chess.empty],
            "row4": [Chess.empty, Chess.empty, Chess.empty, Chess.empty, Chess.empty],
            "row5": [Chess.empty, Chess.empty, Chess.empty, Chess.empty, Chess.empty]
        }

    # method to determine if there is a win
    def judging(self, chess):
        # check vertical win cases
        for i in range(0, 5):
            if self.__fields["row1"][i] == chess and self.__fields["row2"][i] == chess and self.__fields["row3"][i] == chess and self.__fields["row4"][i] == chess and self.__fields["row5"][i] == chess:
                return True

        # check horizontal win cases
        for value in self.__fields.values():
            if value[0] == chess and value[1] == chess and value[2] == chess and value[3] == chess and value[4] == chess:
                return True

        # check diagonal win cases
        if self.__fields["row1"][0] == chess and self.__fields["row2"][1] == chess and self.__fields["row3"][2] == chess and self.__fields["row4"][3] == chess and self.__fields["row5"][4] == chess:
            return True
        
        if self.__fields["row5"][0] == chess and self.__fields["row4"][1] == chess and self.__fields["row3"][2] == chess and self.__fields["row2"][3] == chess and self.__fields["row1"][4] == chess:
            return True

        # no win condition met
        return False