# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    return -1

# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))



def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # type here
    
    n = len(stops)
    curr_refill, num_refill, limit = 0, 0, m

    while limit < d:
        if curr_refill >= n or stops[curr_refill] > limit:
            return -1

        # Safe move: find farthest possible point to refill
        for i in range(curr_refill, n):
            if stops[i] <= limit:
                curr_refill = i

        limit = stops[curr_refill] + m
        curr_refill += 1
        num_refill += 1

    return num_refill



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n
    print(compute_min_number_of_refills(input_d, input_m, input_stops))
