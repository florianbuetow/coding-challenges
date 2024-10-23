def transpose_matrix(matrix: list[list[int|float]]) -> list[list[int|float]]:    
    # O(width * height) time and space
    width, height = len(matrix[0]), len(matrix)
    transposed_matrix = [[0] * height for _ in range(width)]
    for col in range(width):
        for row in range(height):
            transposed_matrix[col][row] = matrix[row][col]
    return transposed_matrix