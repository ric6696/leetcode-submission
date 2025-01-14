import sys


def findThePrefixCommonArray(a, b):
    mp = {}
    res = []
    for i in range(0, len(a)):
        cnt = 0
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1

        for j in range(0, i + 1):
            if b[j] in mp:
                cnt += 1
        res.append(cnt)

    return res


def findThePrefixCommonArrayFast(A, B):
    res = []
    a, b = set(), set()
    count = 0
    for i in range(0, len(A)):
        a.add(A[i])
        b.add(B[i])
        if A[i] == B[i]:
            count += 1
            res.append(count)
            continue
        if A[i] in b:
            count += 1
        if B[i] in a:
            count += 1
        res.append(count)

    return res


def main():
    a = [1, 3, 2, 4]
    b = [3, 1, 2, 4]
    # print(findThePrefixCommonArray(a, b))
    print(findThePrefixCommonArrayFast(a, b))


if __name__ == "__main__":
    sys.exit(main())
