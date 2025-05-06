import sys


def numEquivDominoPairsHash(dominoes):
    mpp = [0] * 100
    count = 0
    for a, b in dominoes:
        key = a * 10 + b if a <= b else b * 10 + a
        count += mpp[key]
        mpp[key] += 1
    return count


def numEquivDominoPairsBrute(dominoes):
    count = 0
    for i in range(len(dominoes)):
        for j in range(i + 1, len(dominoes)):
            a, b = dominoes[i]
            c, d = dominoes[j]
            if (a == c and b == d) or (a == d and b == c):
                count += 1
    return count


def main():
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6], [4, 3], [4, 3]]
    # print(numEquivDominoPairsBrute(dominoes))
    print(numEquivDominoPairsHash(dominoes))


if __name__ == "__main__":
    sys.exit(main())
