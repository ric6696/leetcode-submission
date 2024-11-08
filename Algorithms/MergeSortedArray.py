import sys


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[idx] = nums2[n - 1]
                n -= 1
            else:
                nums1[idx] = nums1[m - 1]
                m -= 1
            idx -= 1

        while n > 0:
            nums1[idx] = nums2[n - 1]
            n -= 1
            idx -= 1


def main():
    solution = Solution()
    nums1, nums2 = [4, 5, 6, 0, 0, 0], [1, 2, 3]
    m, n = 3, 3

    print(f"Before Merging: {nums1}")
    solution.merge(nums1, m, nums2, n)
    print(f"After Merging: {nums1}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
