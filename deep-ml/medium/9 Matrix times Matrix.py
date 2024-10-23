import numpy as np
def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]: 
    # O(n^3) time and O(n^2) space
    
    # convert arrays to numpy arrays
    A = np.array(a)
    B = np.array(b)
    try:
        # perform a matrix multiplication
        return np.dot(A, B)
    except:
        # in case of matrix dimensions mismatch
        return -1
