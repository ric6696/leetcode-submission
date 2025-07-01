import sys
from typing import DefaultDict


def groupAnagrams(strs):
    res = DefaultDict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return list(res.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

    # Expected Output
    # [["bat"],["nat","tan"],["ate","eat","tea"]]


if __name__ == "__main__":
    sys.exit(main())
