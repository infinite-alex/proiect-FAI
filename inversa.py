def minor(matrix, row, col):
    result = []
    for i in range (len(matrix)):
        if i == row:
            continue
        new_row = []
        for j in range (len(matrix[i])):
            if j != col:
                new_row.append(matrix[i][j])
        result.append(new_row)

    return result

def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def cofactor(matrix, i, j):
    minor_det = determinant(minor(matrix, i, j))
    return (-1)**(i+j) * minor_det

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return determinant_2x2(matrix)
    
    det = 0
    for j in range(len(matrix)):
        det += matrix[0][j] * cofactor(matrix, 0, j)
    return det

def adjugata(matrix):
    size = len(matrix)

    cofactor_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(cofactor(matrix, i, j))
        cofactor_matrix.append(row)

    new_matrix = []
    for j in range(size):
        new_row = []
        for i in range(size):
            new_row.append(cofactor_matrix[i][j])
        new_matrix.append(new_row)

    return new_matrix


def inversa(matrix):
    
    if len(matrix) == 1:
       return 1 / matrix[0]
    
    if len(matrix) != len(matrix[0]):
        return "Matricea nu este patratica"
    
    det = determinant(matrix)
    if det == 0:
        return "determinant zero -> matricea nu are inversa"
    
    adj = adjugata(matrix)
    size = len(matrix)
    inversa = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(adj[i][j] / det)
        inversa.append(row)

    return inversa




