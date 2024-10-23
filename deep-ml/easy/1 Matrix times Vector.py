def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    # O(n*m) time and O(m) space, NxM = dim of matrix
    # source: https://www.deep-ml.com/problem/Matrix%20times%20Vector

    if len(a[0]) != len(b):
        # matrix width has to match vector length
        return -1

    c = []
    for row in a:
        c.append(sum(x * y for x, y in zip(row, b)))
    return c
