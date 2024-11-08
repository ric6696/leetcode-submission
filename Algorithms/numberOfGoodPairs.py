import sys


def numIdenticalPairs(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                cnt += 1

    return cnt


def main():
    nums = [1, 2, 3, 1, 1, 3]
    nums2 = [1, 1, 1, 1]
    print(numIdenticalPairs(nums))
    print(numIdenticalPairs(nums2))


if __name__ == "__main__":
    sys.exit(main())
