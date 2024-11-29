import sys


def maxProfit(prices):
    maxProfit = 0
    for i in range(0, len(prices) - 1):
        if prices[i] > prices[i + 1]:
            continue
        else:
            maxProfit += prices[i + 1] - prices[i]

    return maxProfit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


if __name__ == "__main__":
    sys.exit(main())
