import sys


# Sliding Window
def countSubarrays(arr, k):
    num = max(arr)
    cnt = 0
    left = 0
    res = 0

    for right in range(len(arr)):
        if arr[right] == num:
            cnt += 1
        while cnt >= k:
            if arr[left] == num:
                cnt -= 1
            left += 1
        res += left

    return res


def main():
    arr = [1, 3, 2, 3, 3]
    k = 2
    print(countSubarrays(arr, k))  # Output: 7


if __name__ == "__main__":
    sys.exit(main())
