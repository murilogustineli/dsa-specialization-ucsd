# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     print(*points)



Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    # type here
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)

    for i in segments:
        if current < i.start:
            current = i.end
            points.append(current)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = compute_optimal_points(segments)
    print(len(points))
    print(*points)
