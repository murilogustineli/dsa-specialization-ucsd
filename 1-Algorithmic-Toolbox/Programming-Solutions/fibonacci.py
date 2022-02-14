# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonacci_number(n):
    assert 0 <= n <= 45         # Check weather n is between 0 and 45
    a, b = 0, 1                 # Assigning values to variables a and b
    add = 0                     # Assigning value to variable add
    if n <= 1:
        return n
    else:
        for i in range(n-1):
            add = a + b         # Sum a and b
            a = b               # Update value of a
            b = add             # Update value of b
        return add


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
    # print(fibonacci_number_naive(40))
