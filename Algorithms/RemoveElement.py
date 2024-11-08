import sys


def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return nums


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElement(nums, val))
    return 0


if __name__ == "__main__":
    sys.exit(main())
