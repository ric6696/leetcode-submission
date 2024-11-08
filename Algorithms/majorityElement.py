import sys


def majorityElement(nums):
    map = {}
    for n in nums:
        if n not in map:
            count = 0
            map[n] = count
        map[n] = map[n] + 1

    max_key = max(map, key=map.get)
    return max_key


def main():
    print("Enter the elements of the list: ")
    nums = [2, 2, 1, 1, 1, 2, 2, 4]

    print(majorityElement(nums))


if __name__ == "__main__":
    sys.exit(main())
