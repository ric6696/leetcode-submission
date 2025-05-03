import sys


def lln(nums, n, m, k):
    """ """
    total = 0
    nums.sort()

    cntSecMax = m % k  # number of second max needed
    cntMaxIteration = m // k  # how many groups of max iteration of k needed
    cntMax = cntMaxIteration * k  # total number of max needed
    total = cntMax * nums[n - 1] + nums[n - 2] * cntSecMax

    return total


def lln2(nums, n, m, k):
    result = 0
    nums.sort()

    first = nums[n - 1]
    second = nums[n - 2]

    # number of max needed
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result += (count) * first
    result += (m - count) * second

    return result


def main():
    nums = [3, 4, 3, 4, 3]
    n = 5
    m = 7
    k = 2
    print(lln(nums, n, m, k))


if __name__ == "__main__":
    sys.exit(main())
