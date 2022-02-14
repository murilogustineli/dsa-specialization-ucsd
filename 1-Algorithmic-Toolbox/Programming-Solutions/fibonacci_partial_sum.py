# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


# if __name__ == '__main__':
#     input = sys.stdin.read();
#     from_, to = map(int, input.split())
#     print(fibonacci_partial_sum_naive(from_, to))


def last_digit_sum_fibonacci(n):
    assert 0 <= n <= 10 ** 18
    a, b = 0, 1

    # Pisano period of mod 10 is 60
    n = n % 60

    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(0, n+1):
        a, b = b, (a + b) % 60
    last_num = b - 1

    return last_num % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    # type here
    m, n = from_index, to_index
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if m == 0:
        final = last_digit_sum_fibonacci(n) - last_digit_sum_fibonacci(m)
    else:
        final = last_digit_sum_fibonacci(n) - last_digit_sum_fibonacci(m-1)
    return final % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
    