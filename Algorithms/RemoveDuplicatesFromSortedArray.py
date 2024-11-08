import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                print(len(nums))
            i += 1
        print(nums)
        return len(nums)


def main():
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3]
    print(solution.removeDuplicates(nums))

    return 0


if __name__ == "__main__":
    sys.exit(main())
