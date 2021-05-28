# *****
# A class to log moves to a file.
# *****

class Logger:
    """A class to represent the logger."""

    def log(self, text, filename):
        # try to write to the filename specified
        try:
            # append to the filename the line of text specified
            with open(filename, 'a') as logFile:
                logFile.write(text)
        # catch a FileNotFoundError
        except FileNotFoundError:
            print("The file could not be found.")