def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = []
    for row in matrix:
        result.append([val * scalar for val in row])
    return result