import sys


def findWordsContaining(words, x):
    res = []
    for i, n in enumerate(words):
        if x in n:
            res.append(i)
    return res


def main():
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "a"
    print(findWordsContaining(words, x))


if __name__ == "__main__":
    sys.exit(main())
