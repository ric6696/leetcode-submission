import sys


def threeConsecutiveOdds(arr):
    for i in range(len(arr) - 2):
        if arr[i] % 2 != 0:
            if arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
    return False


def main():
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    arr2 = [5, 3]
    print(threeConsecutiveOdds(arr))
    print(threeConsecutiveOdds(arr2))


if __name__ == "__main__":
    sys.exit(main())
