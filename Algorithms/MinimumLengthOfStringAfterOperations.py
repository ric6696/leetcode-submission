import sys


def minimumLength(s):
    c = set(s)
    mp, res = {}, 0

    for char in s:
        if char in mp:
            mp[char] += 1
        else:
            mp[char] = 1

    for k in c:
        while mp[k] > 2:
            mp[k] -= 2
        res += mp[k]

    return res


def main():
    s = "abaacbcbb"
    print(minimumLength(s))


if __name__ == "__main__":
    sys.exit(main())
