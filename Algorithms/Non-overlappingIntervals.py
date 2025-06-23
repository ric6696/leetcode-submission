import sys


def eraseOverIntervals(intervals):
    res = 0
    intervals = sorted(intervals, key=lambda x: x[0])
    prevEnd = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prevEnd:
            res += 1
            prevEnd = min(prevEnd, intervals[i][1])
        else:
            prevEnd = intervals[i][1]

    return res


def main():
    n = int(input("Intervals: "))
    intervals = [
        list(map(int, input("Intervals e.g. 1 3: ").split())) for _ in range(n)
    ]
    print(eraseOverIntervals(intervals))


if "__main__" == __name__:
    sys.exit(main())
