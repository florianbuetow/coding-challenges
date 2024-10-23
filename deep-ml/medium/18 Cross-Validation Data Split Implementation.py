import numpy as np
def cross_validation_split(data: np.ndarray, k: int) -> list:
    # split data into k (approximately) equal parts
    np.random.shuffle(data)
    folds = np.array_split(data, k) # doesn't split it the same way the solution wants

    # create k cross-validation test-train-sets
    result = []
    for i in range(k):
        # select fold i as the test set
        test_set = folds[i]
        # merge all other folds into a training set
        train_folds = [folds[j] for j in range(k) if j != i]
        train_set = np.concatenate(train_folds)

        # I would prefer to yield here
        result.append((train_set, test_set))
    return result
