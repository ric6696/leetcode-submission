import sys


def lengthOfLastWord(s):
    lastIdx = len(s) - 1

    if s[lastIdx] == " ":
        while s[lastIdx] == " ":
            lastIdx -= 1

    lastWord = 0
    while s[lastIdx] != " ":
        if lastIdx == 0:
            return 1 + lastWord
        lastIdx -= 1
        lastWord += 1

    return lastWord


def main():
    s = "   fly me   to   the moon  "
    s1 = "Hello World"
    s2 = "luffy is still joyboy"
    s3 = "day"
    print(lengthOfLastWord(s))
    print(lengthOfLastWord(s1))
    print(lengthOfLastWord(s2))
    print(lengthOfLastWord(s3))


if __name__ == "__main__":
    sys.exit(main())
