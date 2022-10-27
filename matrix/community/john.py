class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [map(int, r.split()) for r in matrix_string.split("\n")]

    @property
    def rows(self):
        return self._matrix[:]

    @property
    def columns(self):
        return map(list, zip(*self._matrix))
