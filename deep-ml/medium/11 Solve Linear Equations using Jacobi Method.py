import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    """
    Calculates an approximate solution for the system of 
    linear equations Ax = b using the Jacobi method:

        x' := (b - Rx) / D

        1. Start with an initial guess for the solution vector x.
        2. Compute an approximation x' of x using the above formula
        3. Repeat n times (hoping for conversion)

    """

    x = np.zeros_like(b, dtype=np.float64) # initial guess of the solution
    D = np.diag(A) # diagonal of A as a vector
    R = A - np.diagflat(D) # A without its diagonal

    for _ in range(n):
        # Calculate the next approximation of x using the formula:
        # x[i]' := (b[i] - R[i,j]*x[j]) / D[i], for j=1...len(b)
        x = np.round((b - np.dot(R, x)) / D, 4)
    return x.tolist()