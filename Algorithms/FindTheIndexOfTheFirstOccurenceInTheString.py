import sys


def strStr(haystack, needle):
    if len(haystack) < len(needle) or needle not in haystack:
        return -1

    for j in range(0, len(haystack)):
        tmp = ""
        if needle[0] == haystack[j]:
            tmp += haystack[j : j + len(needle)]
            if tmp in needle:
                return j

        # n = len(needle)
        # for i in range(len(haystack)-n+1):
        # if needle == haystack[i:i+n]
        # return i
        # return -1


def main():
    haystack = "mississippi"
    needle = "issip"

    print(strStr(haystack, needle))
    return


if __name__ == "__main__":
    sys.exit(main())
