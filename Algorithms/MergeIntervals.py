import sys


def merge(intervals):
    output = []
    intervals = sorted(intervals, key=lambda x: x[0])
    output.append(intervals[0])

    for i in range(1, len(intervals)):
        if output[-1][1] >= intervals[i][0]:
            output[-1][1] = max(output[-1][1], intervals[i][1])
        else:
            output.append(intervals[i])

    return output


def main():
    n = int(input("Enter number of Intervals: "))
    intervals = [
        list(map(int, input("Enter Intervals, e.g. 1 3: ").split())) for _ in range(n)
    ]
    print(merge(intervals))


if __name__ == "__main__":
    sys.exit(main())
