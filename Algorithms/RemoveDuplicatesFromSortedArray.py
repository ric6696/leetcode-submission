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

    def removeDuplicatesArray(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return nums[:l]


def main():
    solution = Solution()
    nums = [0, 0, 5, 3, 2, 6, 8, 8, 8]
    print(solution.removeDuplicates(nums))
    print(solution.removeDuplicatesArray(nums))

    return 0


if __name__ == "__main__":
    sys.exit(main())
