import sys


def longestMonotonicSubarray(nums):
    minMax, maxMax = 1, 1
    cnt, mcnt = 1, 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            cnt += 1
        if nums[i - 1] >= nums[i] or i == len(nums) - 1:
            if cnt > maxMax:
                maxMax = cnt
            cnt = 1

    for j in range(1, len(nums)):
        if nums[j - 1] > nums[j]:
            mcnt += 1
        if nums[j - 1] <= nums[j] or j == len(nums) - 1:
            if mcnt > minMax:
                minMax = mcnt
            mcnt = 1

    return max(maxMax, minMax)


def main():
    nums = [3, 2, 1]
    print(longestMonotonicSubarray(nums))


if __name__ == "__main__":
    sys.exit(main())
