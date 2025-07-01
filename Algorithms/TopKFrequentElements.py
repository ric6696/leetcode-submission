import sys


def topKFrequent(nums: list[int], k: int):
    mp = {}
    res = []
    for n in nums:
        if n in mp:
            mp[n] += 1
        else:
            mp[n] = 1

    while k:
        max_key = max(mp, key=mp.get)
        res.append(max_key)
        mp[max_key] = 0
        k -= 1

    return res


def main():
    nums = list(map(int, input("Enter an array: ").split()))
    k = int(input("Enter k: "))
    print(topKFrequent(nums, k))


if __name__ == "__main__":
    sys.exit(main())
