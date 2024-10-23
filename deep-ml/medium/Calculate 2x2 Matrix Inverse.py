import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    # convert to 2d numpy array
    matrix = np.array(matrix)
    try:
        # return the inverse of the matrix
        return np.linalg.inv(matrix)
    except: # not invertible
        return None