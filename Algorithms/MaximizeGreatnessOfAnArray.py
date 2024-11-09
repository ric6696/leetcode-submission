import sys


def maximizeGreatness(nums):
    nums.sort()

    res = 0

    for x in nums:
        if x > nums[res]:
            res += 1
    return res


def main():
    arr = [1, 3, 5, 2, 1, 3, 1]
    print(maximizeGreatness(arr))


if __name__ == "__main__":
    sys.exit(main())
