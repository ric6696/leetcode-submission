import sys


def finalPrices(prices):
    res = []
    for i in range(0, len(prices)):
        discount = 0
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                discount = prices[j]
                break
        res.append(prices[i] - discount)
    return res


def finalPricesMonotonic(prices):
    stack = []
    for i, num in enumerate(prices):
        while stack and prices[stack[-1]] > num:
            popIndex = stack.pop()
            prices[popIndex] -= num
        stack.append(i)
    return prices


def main():
    prices = [8, 4, 6, 2, 3]
    # print(finalPrices(prices))
    print(finalPricesMonotonic(prices))


if __name__ == "__main__":
    sys.exit(main())
