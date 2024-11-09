import sys


def maximumTotalSum(maximumHeight):
    maximumHeight.sort(reverse=True)
    sum = maximumHeight[0]

    for i in range(len(maximumHeight) - 1):
        if maximumHeight[i + 1] >= maximumHeight[i]:
            maximumHeight[i + 1] = maximumHeight[i] - 1
            sum += maximumHeight[i + 1]
            if maximumHeight[i + 1] == 0:
                return -1
        else:
            sum += maximumHeight[i + 1]

    return sum


def main():
    maximumHeight = [2, 3, 4, 3]
    print(maximumTotalSum((maximumHeight)))


if __name__ == "__main__":
    sys.exit(main())
