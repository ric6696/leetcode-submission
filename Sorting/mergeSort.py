import sys


def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2

        leftArray = nums[:mid]
        rightArray = nums[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                nums[k] = leftArray[i]
                i += 1
            else:
                nums[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            nums[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            nums[k] = rightArray[j]
            j += 1
            k += 1

        print(nums)


def main():
    nums = [6, 4, 3, 8, 1, 5, 2, 7]
    mergeSort(nums)
    return 0


if __name__ == "__main__":
    sys.exit(main())
