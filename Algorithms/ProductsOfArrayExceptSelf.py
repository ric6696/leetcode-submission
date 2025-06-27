import sys


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix, suffix, res = n * [1], n * [1], n * [1]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix[n - i - 1] = suffix[n - i] * nums[n - i]

    for i in range(n):
        res[i] = prefix[i] * suffix[i]

    return res


def main():
    nums = list(map(int, input("Enter nums: ").split()))
    print(productExceptSelf(nums))


if "__main__" == __name__:
    sys.exit(main())
