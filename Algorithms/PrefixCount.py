import sys


def prefixCount(words, pref):
    cnt = 0
    n = len(pref)
    for word in words:
        if pref in word[0:n]:
            cnt += 1
    return cnt


def prefixCount2(words, pref):
    cnt = 0
    for word in words:
        if word.startswith(pref):
            cnt += 1
    return cnt


def main():
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    # print(prefixCount(words, pref))
    print(prefixCount2(words, pref))


if "__main__" == __name__:
    sys.exit(main())
