import sys


def maxScore(nums):
    nums.sort(reverse=True)
    if nums[0] <= 0:
        return 0

    n, cnt = 0, 1
    while n < len(nums) - 1:
        nums[n + 1] = nums[n] + nums[n + 1]
        if nums[n + 1] > 0:
            cnt += 1
        n += 1
    return cnt


def main():
    nums = [2, -1, 0, 1, -3, 3, -3]
    print(maxScore(nums))


if __name__ == "__main__":
    sys.exit(main())
