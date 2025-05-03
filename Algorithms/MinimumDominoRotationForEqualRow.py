import sys


def cntRotations(tops, bottoms):
    mp_t = {}
    count = 0

    for t in tops:
        if t in mp_t:
            mp_t[t] += 1
        else:
            mp_t[t] = 1
    maxKey = max(mp_t, key=mp_t.get)

    for x in range(len(tops)):
        if tops[x] == maxKey:
            continue
        elif tops[x] != maxKey & bottoms[x] == maxKey:
            count += 1
        else:
            return -1

    return count


def minDominoRotations(tops, bottoms):
    first = cntRotations(tops, bottoms)
    second = cntRotations(bottoms, tops)

    if (first == -1) & (second == -1):
        return -1
    elif (first == -1) & (second != -1):
        return second
    elif (first != -1) & (second == -1):
        return first
    else:
        return min(first, second)


# Other Solution using brute-force implementation


def minDominoRotationsBrute(tops, bottoms):
    res = getRotation(tops, bottoms, tops[0])
    if bottoms[0] != tops[0]:
        getRotation(tops, bottoms, bottoms[0])
        res = min(res, getRotation(tops, bottoms, bottoms[0]))
    return -1 if res == float("inf") else res


def getRotation(tops, bottoms, target):
    rotateTop = rotateBottom = 0
    for i in range(len(tops)):
        if tops[i] != target and bottoms[i] != target:
            return float("inf")
        if tops[i] != target:
            rotateTop += 1
        if bottoms[i] != target:
            rotateBottom += 1
    print(rotateTop, rotateBottom)
    return min(rotateTop, rotateBottom)


def main():
    tops = [1, 2, 1, 1, 1, 2, 2, 2]
    bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
    # print(minDominoRotations(tops, bottoms))
    print(minDominoRotationsBrute(tops, bottoms))


if __name__ == "__main__":
    sys.exit(main())
