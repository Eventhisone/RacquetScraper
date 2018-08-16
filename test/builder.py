from racquet import Racquet

class Builder:
    """Builds a tennis racquet object"""

    def fromTextFile(filename):
        txtFile = open(filename, "r")
        racquetObjArray = []
        

        