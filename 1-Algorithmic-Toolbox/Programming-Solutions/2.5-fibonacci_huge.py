# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))


# Compute and return pisano period
def pisano(m):
    previous, current = 0, 1

    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # Pisano period always stars with 01
        if (previous == 0 and current == 1):
            return i + 1


# Compute the N-th Fibonacci number modulo M
def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    previous, current = 0, 1

    # Getting the period
    pisanoPeriod = pisano(m)

    # Taking mod of N with period length
    n = n % pisanoPeriod

    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Compute Fibonacci number
    for i in range(0, n-1):
        previous, current = current, (previous + current)

    return current % m


## Debuging
# from itertools import product
# def test_small():
#     for n, m in product(range(2, 15), repeat=2):
#         print(n, m, fibonacci_number_again_naive(n, m), fibonacci_number_again(n, m))
# test_small()

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
