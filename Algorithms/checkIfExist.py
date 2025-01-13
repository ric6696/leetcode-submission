import sys


def checkIfExist(arr):
    map = {}
    for num in arr:
        if num * 2 in map or num / 2 in map:
            return True
        else:
            map[num] = True
    return False


def main():
    arr = [10, 2, 5, 3]
    print(checkIfExist(arr))


if __name__ == "__main__":
    sys.exit(main())
