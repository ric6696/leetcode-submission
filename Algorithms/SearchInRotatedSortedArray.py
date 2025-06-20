import sys


def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        if nums[mid] > nums[left]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


def main():
    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(search(nums, target))


if "__main__" == __name__:
    sys.exit(main())
