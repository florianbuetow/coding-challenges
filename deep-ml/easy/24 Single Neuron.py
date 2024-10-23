import math
def sigmoid(x):
    return  1 / (1 + math.exp(-x))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    result, mse = [], 0
    for feature_vector, label in zip(features, labels):
        summ = sum(f * w for f, w in zip (feature_vector, weights)) + bias
        prediction = sigmoid(summ)
        mse += (label - prediction) ** 2
        result.append(round(prediction, 4))
    mse = round(mse / len(features), 4)
    return result, mse