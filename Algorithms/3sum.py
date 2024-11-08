import sys


def threeSum(nums):
    res = []
    x = []
    nums.sort()

    for i in range(0, len(nums) - 2):
        if nums[i] in x:
            continue
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if (
                    nums[i] + nums[j] + nums[k] == 0
                    and [nums[i], nums[j], nums[k]] not in res
                ):
                    x.append(nums[i])
                    res.append([nums[i], nums[j], nums[k]])

    return res
    # Current Solution is not optimal, because it is not able to handle large inputs
    # The time complexity of the current solution is O(n^3)
    # Solution: We can use two pointer approach to solve this problem


def threeSumOptimal(nums):
    res = []
    nums.sort()

    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSumOptimal(nums))


if __name__ == "__main__":
    sys.exit(main())
