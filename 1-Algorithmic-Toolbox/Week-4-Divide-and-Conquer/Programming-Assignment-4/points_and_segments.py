# Uses python3
import sys
import collections


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)

    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    for i in ends:
        pairs.append((i, right_label))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    coverage = 0
    for pair in sorted_pairs:
        if pair[1] == left_label:
            coverage += 1
        if pair[1] == right_label:
            coverage -= 1
        if pair[1] == point_label:
            indices = points_map[pair[0]]
            for i in indices:
                count[i] = coverage

    return count


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
