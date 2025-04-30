import sys
import math


def findNumbers(nums):
    res = 0
    for n in nums:
        cnt = 0
        while n >= 1:
            n = n / 10
            cnt += 1
        if cnt % 2 == 0:
            res += 1
    return res


# Using math library log
def findNumbersMath(nums):
    res = 0
    for n in nums:
        if (int(math.log10(n)) + 1) % 2 == 0:
            res += 1

    return res


def main():
    nums = [555, 901, 482, 1771]
    print(findNumbers(nums))
    print(findNumbersMath(nums))


if __name__ == "__main__":
    sys.exit(main())
