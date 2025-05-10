import sys


def minSum(nums1, nums2):
    sum1, sum2 = 0, 0
    numzero1, numzero2 = 0, 0

    for n in nums1:
        if n == 0:
            numzero1 += 1
        else:
            sum1 += n

    for n in nums2:
        if n == 0:
            numzero2 += 1
        else:
            sum2 += n

    min1 = sum1 + numzero1
    min2 = sum2 + numzero2

    if numzero1 == 0 and numzero2 == 0:
        return sum1 if sum1 == sum2 else -1
    if numzero1 == 0:
        return sum1 if min2 <= sum1 else -1
    if numzero2 == 0:
        return sum2 if min1 <= sum2 else -1

    return max(min1, min2)

    # minMp = {}

    # maxMp = {}
    # maxMp[0] = 0

    # minNum = nums2 if sum(nums1) > sum(nums2) else nums1
    # maxNum = nums1 if sum(nums1) > sum(nums2) else nums2

    # if 0 in minNum:
    #     for n in minNum:
    #         if n in minMp:
    #             minMp[n] += 1
    #         else:
    #             minMp[n] = 1

    #     for n in maxNum:
    #         if n in maxMp:
    #             maxMp[n] += 1
    #         else:
    #             maxMp[n] = 1

    #     maxMin = sum(minNum) + 1 * minMp[0]
    #     maxMax = sum(maxNum) + 1 * maxMp[0]

    #     if maxMin <= maxMax:
    #         return maxMax
    # return -1


def main():
    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]
    print(minSum(nums1, nums2))


if __name__ == "__main__":
    sys.exit(main())
