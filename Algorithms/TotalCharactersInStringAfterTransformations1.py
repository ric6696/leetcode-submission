import sys
import string
from string import ascii_lowercase


# Gets Time limit Exceed Error using dictionary with alphabet from a to z
def lengthAfterTransformations(s, t):
    mp = dict.fromkeys(string.ascii_lowercase, 0)
    for i in range(len(s)):
        if s[i] in mp:
            mp[s[i]] += 1

    for _ in range(t):
        tmp = dict.fromkeys(string.ascii_lowercase, 0)
        for c in ascii_lowercase:
            if c == "z":
                tmp["a"] = (tmp["a"] + mp["z"]) % (10**9 + 7)
                tmp["b"] = (tmp["b"] + mp["z"]) % (10**9 + 7)
            else:
                tmp[chr(ord(c) + 1)] = (tmp[chr(ord(c) + 1)] + mp[chr(ord(c))]) % (
                    10**9 + 7
                )
        mp = tmp

    cnt = 0
    for c in ascii_lowercase:
        cnt += mp[c]
    return cnt % (10**9 + 7)


# Using Array List instead of dictionary
def lengthAfterTransformationsArr(s, t):
    MOD = 10**9 + 7
    mp = [0] * 26
    for c in s:
        mp[ord(c) - ord("a")] += 1

    for _ in range(t):
        tmp = [0] * 26
        for i in range(26):
            if i == 25:
                tmp[0] = (tmp[0] + mp[25]) % MOD
                tmp[1] = (tmp[1] + mp[25]) % MOD
            else:
                tmp[i + 1] = (tmp[i + 1] + mp[i]) % MOD
    return sum(mp) % MOD


def main():
    s = input("Enter a string: ")  # jqktcurgdvlibczdsvnsg
    t = int(input("Enter a number: "))  # 7517
    print(lengthAfterTransformations(s, t))


if __name__ == "__main__":
    sys.exit(main())


# abc t = 3
# a:1 b:1 c:1

#
