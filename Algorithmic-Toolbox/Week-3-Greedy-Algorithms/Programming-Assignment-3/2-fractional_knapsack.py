# Uses python3
import sys
from sys import stdin

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


# if __name__ == "__main__":
#     data = list(map(int, sys.stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))



def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # type here
    max_val, knapsack, total = 0, 0, 0

    # While knapsack is not full
    while knapsack < capacity:
        # Choose item with maximum vi/wi
        for i in range(len(prices)):
            if prices[i]/weights[i] >= prices[max_val]/weights[max_val]:
                max_val = i

        # If item fits into knapsack, take all of it
        if knapsack + weights[max_val] <= capacity:
            total += prices[max_val]
            knapsack += weights[max_val]
        else:
            total = total + ((capacity - knapsack) * (prices[max_val]/weights[max_val]))
            knapsack = knapsack + (capacity - knapsack)

        weights.pop(max_val)
        prices.pop(max_val)
        max_val = 0

        if len(prices) == 0:
            break

    return float(round(total, 4))


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
