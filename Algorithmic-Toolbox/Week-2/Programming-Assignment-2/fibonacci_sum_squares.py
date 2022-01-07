# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

# if __name__ == '__main__':
#     n = int(stdin.read())
#     print(fibonacci_sum_squares_naive(n))


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    # type here
    a, b = 0, 1
    sqr = 1
    # Pisano period of mod 10 is 60
    n = n % 60

    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(2, n+1):
        a, b = b, ((a + b)) % 60
        sqr += b**2
    last_num = (sqr % 10)

    return last_num

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
    