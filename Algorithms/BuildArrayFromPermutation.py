import sys


def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for idx in range(len(nums)):
        ans.append(nums[nums[idx]])
    return ans


def main():
    nums = [5, 0, 1, 2, 3, 4]
    print(buildArray(nums))


if __name__ == "__main__":
    sys.exit(main())
