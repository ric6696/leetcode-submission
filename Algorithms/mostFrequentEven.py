import sys


def mostFrequentEven(nums):
    map = {}
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            if nums[i] in map:
                map[nums[i]] = map[nums[i]] + 1
            else:
                map[nums[i]] = 1
    if not map:
        return -1

    val = 10**6
    cnt = 0

    for key in map:
        if map[key] > cnt or map[key] == cnt:
            val = key
            cnt = map[key]
    return val


def main():
    nums = [0, 1, 2, 2, 4, 4, 1]
    oddnums = [1, 3, 5, 7, 7, 7]
    print(mostFrequentEven(nums))
    print(mostFrequentEven(oddnums))
    return


if __name__ == "__main__":
    sys.exit(main())
