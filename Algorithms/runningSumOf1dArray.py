import sys


def runningSumOf1dArray(nums):
    res = []
    for i in range(len(nums)):
        res.append(sum(nums[0 : i + 1]))
    return res


def main():
    nums = [3, 1, 2, 10, 1]
    print(runningSumOf1dArray(nums))
    return


if __name__ == "__main__":
    sys.exit(main())
