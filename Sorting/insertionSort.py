import sys


def insertionSort(arr):
    for i in range(0, len(arr) - 1):
        print(i)
        j = i
        print(f"j: {j}")
        while j >= 0:
            if arr[j + 1] < arr[j]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                j -= 1
            else:
                break
        print(f"{i} attempt: {arr}")
    return 0


def main():
    arrList = [5, 3, 6, 1, 2, 7]
    print(arrList)
    insertionSort(arrList)
    return 0


if __name__ == "__main__":
    sys.exit(main())
