# Uses python3
from sys import stdin
import numpy as np


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    # type here
    if len(values) < 3 or sum(values) % 3 != 0:
        return 0

    count = 0
    target = sum(values) // 3
    matrix = np.zeros(shape=(len(values), (target + 1)))
    # print(matrix)

    for v in range(0, len(values)):
        for item in range(target + 1):
            if values[v] <= item:
                matrix[v][item] = max(matrix[v - 1][item], (matrix[v - 1][item - values[v]] + values[v]))
            else:
                matrix[v][item] = matrix[v - 1][item]
        if matrix[v][item] == target:
            count += 1
    if count < 3:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
