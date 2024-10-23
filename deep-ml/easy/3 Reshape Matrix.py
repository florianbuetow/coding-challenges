import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
	np_matrix = np.array(a)
	np_matrix.reshape(new_shape)
	return np_matrix.tolist()
