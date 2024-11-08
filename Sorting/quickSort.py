import sys


def quickSortAlgorithm(arr):
    quickSort(arr, 0, len(arr)-1)

def partition(arr, low, high, pivot):
    l = low
    h = high
    while l<=h: 
        while arr[l] < pivot:
            l += 1
        while arr[h] > pivot:
            h -= 1
    
        if l <= h:
            temp = arr[h]
            arr[h] = arr[l]
            arr[l] = temp
            l += 1
            h -= 1

    return l


def quickSort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        pivot = arr[mid]
        index = partition(arr, low, high, pivot)
        quickSort(arr, low, index-1)
        quickSort(arr, index, high)   
    else:
        return 0

def main():
    arrList = [6,3, 1, 4, 2, 7]
    print(arrList)
    quickSortAlgorithm(arrList)
    print(arrList)
    
if __name__ == '__main__':
    sys.exit(main())
