import sys


def shuffleTheArray(nums):
    res = []
    split = len(nums) // 2
    for i in range(len(nums) // 2):
        res.append(nums[i])
        res.append(nums[split])
        split += 1

    return res


def main():
    nums = [2, 5, 1, 3, 4, 7]
    print(shuffleTheArray(nums))
    return


if __name__ == "__main__":
    sys.exit(main())
