import sys


def findEvenNumbers(digits):
    mp = {}
    res = []

    for d in digits:
        if d in mp:
            mp[d] += 1
        else:
            mp[d] = 1

    # exclude the case of leading zero, and time complexity to O(n)
    for n in range(100, 1000):
        num = n
        if n % 2 == 0:
            mpp = {}
            cnt = 0
            while n > 0:
                rema = n % 10
                if rema in mpp:
                    mpp[rema] += 1
                else:
                    mpp[rema] = 1
                n = n // 10

            for key in mpp:
                if (key in mp) and mpp[key] <= mp[key]:
                    cnt += mpp[key]

            if cnt == 3:
                res.append(num)

    return res


def main():
    digits = list(map(int, input().split()))
    print(findEvenNumbers(digits))


if __name__ == "__main__":
    sys.exit(main())
