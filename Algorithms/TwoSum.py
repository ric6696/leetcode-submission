import sys


class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res

    def twoSumFast(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i


def main():
    nums = [3, 2, 4]
    target = 6

    solution = Solution()
    print(solution.twoSum(nums, target))
    print(solution.twoSumFast(nums, target))


if "__main__" == __name__:
    sys.exit(main())
