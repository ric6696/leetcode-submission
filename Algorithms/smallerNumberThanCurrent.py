import sys


def smallerNumbersThanCurrent(nums):
    res = []
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            if nums[i] > nums[j]:
                count += 1
        res.append(count)

    return res


def smallerNumbersThanCurrentV2(nums):
    return [sorted(nums).index(i) for i in nums]


def main():
    nums = [6, 5, 4, 8]
    print(smallerNumbersThanCurrent(nums))
    print(smallerNumbersThanCurrentV2(nums))
    return


if __name__ == "__main__":
    sys.exit(main())
