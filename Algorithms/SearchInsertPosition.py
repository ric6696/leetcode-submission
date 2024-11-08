import sys


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target < nums[0]:
        #     return 0

        # i = len(nums) - 1
        # while i >= 0:
        #     if nums[i] > target:
        #         i -= 1
        #     elif nums[i] == target:
        #         return i
        #     else:
        #         i += 1
        #         return i

        # Using Binary Search to insert
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return i


def main():
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    print(solution.searchInsert(nums, target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
