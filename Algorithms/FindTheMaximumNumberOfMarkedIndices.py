import sys


def maxNumOfMarkedIndices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = 0
    left = 0
    nums = sorted(nums)
    # print(nums)
    # print(nums[len(nums)//2])
    if len(nums) % 2 == 0:
        right = len(nums) // 2
    else:
        right = len(nums) // 2 + 1
    for x in range(right, len(nums)):
        if nums[left] * 2 <= nums[x]:
            cnt += 2
            left += 1
    return cnt


def main():
    nums = [9, 2, 5, 4]
    print(maxNumOfMarkedIndices(nums))


if __name__ == "__main__":
    sys.exit(main())
