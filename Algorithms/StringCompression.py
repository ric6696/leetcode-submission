import sys


def compress_string(word):
    res = ""
    i, n = 0, len(word)

    while i < n:
        ch = word[i]
        cnt = 1
        while i + 1 < n and word[i + 1] == ch and cnt < 9:
            cnt += 1
            i += 1
        res += str(cnt)
        res += ch
        i += 1

    return res


def main():
    word = "aaaaaaaaaaaaaabb"
    print(compress_string(word))


if __name__ == "__main__":
    sys.exit(main())
