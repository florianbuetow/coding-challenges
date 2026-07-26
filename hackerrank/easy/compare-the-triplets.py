# O(1) time and space
# link: https://www.hackerrank.com/challenges/compare-the-triplets

def compareTriplets(a, b):
    scores = [0, 0]
    for i in range(3):
        if a[i] > b[i]: scores[0] += 1
        if a[i] < b[i]: scores[1] += 1
    return scores
