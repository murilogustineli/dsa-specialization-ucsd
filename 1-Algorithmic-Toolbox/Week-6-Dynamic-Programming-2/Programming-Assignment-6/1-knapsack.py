# Uses python3
# import sys
from sys import stdin
import numpy as np


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     W, n, *w = list(map(int, input.split()))
#     print(optimal_weight(W, w))


# Maximum Amount of Gold
def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # type here
    matrix = np.zeros(shape=(len(weights), (capacity+1)))
    # print(matrix)

    for w in range(0, len(weights)):
        for item in range(capacity+1):
            if weights[w] <= item:
                matrix[w][item] = max(matrix[w-1][item], (matrix[w-1][item - weights[w]] + weights[w]))
            else:
                matrix[w][item] = matrix[w-1][item]
    return int(matrix[-1][-1])


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
