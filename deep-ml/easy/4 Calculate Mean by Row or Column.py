def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode != 'row':
        # transpose matrix
        transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        index = 0
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                val = matrix[row][col]
                t_row, t_col = index // len(transpose[0]), index % len(transpose[0])
                transpose[t_row][t_col] = val
                index += 1
        matrix = transpose
    return [sum(row)/len(row) for row in matrix]

