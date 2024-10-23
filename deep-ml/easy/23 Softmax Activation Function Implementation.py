import numpy as np

def softmax(scores: list[float]) -> list[float]:
    probabilities = np.exp(scores) / np.sum(np.exp(scores))
    return probabilities.tolist()