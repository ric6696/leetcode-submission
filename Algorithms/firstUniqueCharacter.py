import sys


def firstUniqueCharacter(s):
    map = {}
    for i in range(len(s)):
        if s[i] in map:
            map[s[i]] += 1
        else:
            map[s[i]] = 1

    for n in s:
        if map[n] == 1:
            return s.index(n)
    return -1


def main():
    s = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabb"
    print(firstUniqueCharacter(s), firstUniqueCharacter(s2), firstUniqueCharacter(s3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
