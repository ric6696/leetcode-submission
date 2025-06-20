import sys


def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        else:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
    res.append(newInterval)
    return res


def main():
    n = int(input("Enter number of intervals: "))
    intervals = [
        list(map(int, input("Enter Intervals e.g. 1 2: ").split())) for _ in range(n)
    ]
    newInterval = list(map(int, input("Enter New Interval: ").split()))
    print(insert(intervals, newInterval))


if __name__ == "__main__":
    sys.exit(main())
