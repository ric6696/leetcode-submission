import sys


def selectionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def main():
    arrList = [5, 3, 8, 1, 4]
    print(selectionSort(arrList))
    return 0


if __name__ == "__main__":
    sys.exit(main())
