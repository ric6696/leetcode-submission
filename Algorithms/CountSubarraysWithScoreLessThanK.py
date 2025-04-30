import sys


def countSubarrays(nums, k):
    left = 0
    sum = 0
    cnt = 0

    for right in range(len(nums)):
        sum += nums[right]

        # Shrink window if score is too large
        while sum * (right - left + 1) >= k:
            sum -= nums[left]
            left += 1

        # All subarrays ending at `right` and starting from [left, right] are valid
        cnt += right - left + 1

    return cnt


def main():
    nums = [2, 1, 4, 11, 5]
    k = 10
    print(countSubarrays(nums, k))


if __name__ == "__main__":
    sys.exit(main())
