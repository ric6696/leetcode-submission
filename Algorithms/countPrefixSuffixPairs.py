import sys


def isPrefixSuffixPair(word1, word2):
    n, m = len(word1), len(word2)

    if n > m:
        return False
    else:
        for i in range(0, n):
            if word1[i] != word2[i]:
                return False
            elif word1[i] != word2[m - n + i]:
                return False
    return True


def countPrefixSuffixPairs(words):
    cnt = 0
    for i in range(0, len(words)):
        for j in range(i + 1, len(words)):
            if isPrefixSuffixPair(words[i], words[j]) == True:
                cnt += 1
    return cnt


def main():
    words = ["pa", "papa", "ma", "mama"]
    print(countPrefixSuffixPairs(words))


if __name__ == "__main__":
    sys.exit(main())
