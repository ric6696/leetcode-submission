import sys


def minMaxDifference(num):
    maxtarget, mintarget = "9", "0"
    digits = str(num)
    for i in range(len(digits)):
        if digits[i] < "9":
            maxtarget = digits[i]
            break
    max = int(digits.replace(maxtarget, "9"))

    mintarget = digits[0]
    min = int(digits.replace(mintarget, "0"))

    return max - min


def main():
    num = 99999
    print(minMaxDifference(num))


if __name__ == "__main__":
    sys.exit(main())
