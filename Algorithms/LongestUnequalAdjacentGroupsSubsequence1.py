import sys


def getLongestSubsequence(words, groups):
    res = []
    res.append(words[0])

    for i in range(1, len(words)):
        if groups[i - 1] != groups[i]:
            res.append(words[i])

    return res


def main():
    print("Put words array as input: ")
    words = list(map(str, input().split()))
    print("Put groups array as input: ")
    groups = list(map(int, input().split()))
    print(getLongestSubsequence(words, groups))


if __name__ == "__main__":
    sys.exit(main())
