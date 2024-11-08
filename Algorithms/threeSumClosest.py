import sys


def threeSumClosest(nums, target):
    nums.sort()
    min_diff = abs(target - (nums[0] + nums[1] + nums[len(nums) - 1]))
    res = nums[0] + nums[1] + nums[len(nums) - 1]

    print(min_diff)

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            diff = abs(target - sum)
            print(f"diff = {diff}")

            if diff < min_diff:
                min_diff = diff
                res = sum
                print(f"min_diff = {min_diff}")

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return target
    return res


def main():
    nums = [0, 1, 1, 1]
    # [-4, -1, 1, 2]
    target = -100
    print(threeSumClosest(nums, target))
    return


if __name__ == "__main__":
    sys.exit(main())
