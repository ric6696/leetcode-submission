import sys


def containDuplicates(nums):
    map = {}

    for i in nums:
        if i in map:
            return True
        map[i] = i
        print(map)

    return False


def main():
    nums = [5, 4, 8, 3, 3]
    print(containDuplicates(nums))


if __name__ == "__main__":
    sys.exit(main())
