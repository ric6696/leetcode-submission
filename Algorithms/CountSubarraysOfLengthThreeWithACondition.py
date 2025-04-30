import sys


def countSubarrays(nums):
    cnt = 0
    for n in range(2, len(nums)):
        if 2 * (nums[n - 2] + nums[n]) == nums[n - 1]:
            cnt += 1
    return cnt


def main():
    nums = [1, 2, 1, 4, 1]
    print(countSubarrays(nums))


if __name__ == "__main__":
    sys.exit(main())
