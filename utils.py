def transpose(matrix):
    new_matrix = [[], [], [], [], [], []]
    for x in range(0, 7):
        for y in range(0, 6):
            new_matrix[y].append(matrix[x][y])
    return new_matrix