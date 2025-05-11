import sys


def countLargestGroup(n):
    mp = {}
    count = 0

    for k in range(1, n + 1):
        sum = 0
        num = k
        while num != 0:
            sum += num % 10
            num = num // 10
        if sum in mp:
            mp[sum] += 1
        else:
            mp[sum] = 1

    maxKey = max(mp, key=mp.get)

    for j in range(1, len(mp) + 1):
        if mp[j] == mp[maxKey]:
            count += 1

    return count


def main():
    n = int(sys.stdin.readline().strip())
    result = countLargestGroup(n)
    print(result)


if __name__ == "__main__":
    sys.exit(main())
