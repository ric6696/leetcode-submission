import sys


def findClosestNumber(nums):
    minDiff = 10**6
    minIdx = -1
    for i, n in enumerate(nums):
        diff = abs(n - 0)
        if diff <= minDiff:
            if diff == minDiff and (n - 0) < nums[minIdx]:
                continue
            else:
                minDiff = diff
                minIdx = i
    return nums[minIdx]


def main():
    nums = [-4, -2, 1, 4, 8]
    nums2 = [4, -1, 1]
    print(findClosestNumber(nums))
    print(findClosestNumber(nums))


if __name__ == "__main__":
    sys.exit(main())
