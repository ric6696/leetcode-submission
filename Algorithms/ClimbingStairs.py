import sys


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    res = [1, 2]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res[-1]


def climbStairsV2(n):
    one, two = 1, 1

    for i in range(n - 1):
        tmp = one
        one = one + two
        two = tmp
    return one


def main():
    print(climbStairs(5))
    print(climbStairsV2(5))
    return


if __name__ == "__main__":
    sys.exit(main())
