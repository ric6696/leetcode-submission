import sys


# Brute force solution
def mySqrt(x):
    if x == 0:
        return 0

    i = 0
    while i <= x:
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1
        i += 1


# Binary search solution
def mySqrtV2(x):
    left, right = 0, x
    res = 0
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
            res = mid
        else:
            return mid
    return res


def main():
    x = 8
    print(mySqrtV2(x))
    print(mySqrt(x))


if __name__ == "__main__":
    sys.exit(main())
