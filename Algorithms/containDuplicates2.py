import sys


def containDuplicates2(nums, k):
    map = {}
    for i, n in enumerate(nums):
        if n in map and abs(i - map[n]) <= k:
            return True
        map[n] = i
    return False


def main():
    nums = [1, 0, 1, 1]
    k = 1
    print(containDuplicates2(nums, k))


if __name__ == "__main__":
    sys.exit(main())
