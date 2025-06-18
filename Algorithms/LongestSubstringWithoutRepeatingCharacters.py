import sys


def lengthOfLongestSubstring(s):
    max_len = left = 0
    cnt = {}

    for right in range(len(s)):
        if s[right] in cnt:
            cnt[s[right]] += 1
        else:
            cnt[s[right]] = 1

        while cnt[s[right]] > 1:
            cnt[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s = input("Enter a string: ")
    result = lengthOfLongestSubstring(s)
    print(
        f"The length of the longest substring without repeating characters is: {result}"
    )


if __name__ == "__main__":
    sys.exit(main())
