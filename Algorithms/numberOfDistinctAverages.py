import sys


def numberOfDistinctAverages(nums):
    nums = sorted(nums)
    print(nums)

    map = {}
    for i in range(len(nums) // 2):

        avg: float = (nums[0] + nums[len(nums) - 1]) / 2
        if avg not in map:
            map[avg] = avg
        nums.remove(nums[0])
        nums.remove(nums[len(nums) - 1])
    print(map)
    print(nums)

    return len(map)


def main():
    nums = [4, 1, 4, 0, 3, 5]
    print(numberOfDistinctAverages(nums))
    return


if __name__ == "__main__":
    sys.exit(main())
