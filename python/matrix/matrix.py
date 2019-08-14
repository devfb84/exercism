class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(word) for word in line.split()] for line in matrix_string.splitlines()]
        self.columns = [*zip(*self.matrix)]

    def row(self, index):
        return list(self.matrix[index-1])

    def column(self, index):
        return list(self.columns[index-1])
