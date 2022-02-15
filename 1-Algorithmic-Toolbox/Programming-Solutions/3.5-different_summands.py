# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    return summands

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     summands = optimal_summands(n)
#     print(len(summands))
#     for x in summands:
#         print(x, end=' ')



def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    # type here
    k, total = 1, n

    while n > 0:
        n = n - k
        if k+1 > n:
            summands.append(total-sum(summands))
            k += 1
            break
        else:
            summands.append(k)
            k += 1

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
