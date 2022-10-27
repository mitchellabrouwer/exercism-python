def toInt(array):
    return [int(char) for char in array]


def toNumberArray(string):
    return toInt(string.split(" "))


class Matrix:
    def __init__(self, grid):
        self.matrix = list(map(toNumberArray, grid.splitlines()))

    def row(self, index):
        return list([self.matrix[index - 1]])

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
