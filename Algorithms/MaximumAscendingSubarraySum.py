import sys


def maxAscendingSum(nums):
    sum, max = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            sum += nums[i]
        if nums[i - 1] >= nums[i] or i == len(nums) - 1:
            if sum > max:
                max = sum
            sum = nums[i]
    return max


def main():
    nums = [10, 20, 30, 5, 10, 50]
    print(maxAscendingSum(nums))


if __name__ == "__main__":
    sys.exit(main())
