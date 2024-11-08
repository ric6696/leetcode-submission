import sys


def findKthLargest(nums, k):
    left, equal, right = [], [], []
    pivot = nums[len(nums) - 1]
    for n in nums:
        if n < pivot:
            left.append(n)
        elif n == pivot:
            equal.append(n)
        else:
            right.append(n)

    if len(right) == k - 1:
        return equal[0]
    elif len(right) > k - 1:
        return findKthLargest(right, k)
    else:
        return findKthLargest(left, k - len(right) - 1)


def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))
    return


if __name__ == "__main__":
    sys.exit(main())
