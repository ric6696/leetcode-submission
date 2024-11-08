import sys


def bubbleSort(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
        print(f"{i} attempt: {arr}")
        i -= 1

    return 0


def main():
    listArray = [5, 3, 6, 1, 2, 7]
    print(listArray)
    bubbleSort(listArray)
    return 0


if __name__ == "__main__":
    sys.exit(main())
