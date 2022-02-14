# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    # type here
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(gcd_naive(a, b))
