class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []

        for line in matrix_string.splitlines():
            row = []
            for word in line.split():
                row.append(int(word))
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return list([*zip(*self.matrix)][index-1])
