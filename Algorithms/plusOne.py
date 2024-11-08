import sys


def plusOne(digits):
    n = len(digits) - 1
    while n >= 0:
        if digits[n] == 9:
            digits[n] = 0
        else:
            digits[n] += 1
            return digits
        n -= 1
    return [1] + digits


def main():
    digits = [1, 0, 3, 9, 9]
    print(plusOne(digits))
    return 0


if __name__ == "__main__":
    sys.exit(main())
