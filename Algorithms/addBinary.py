import sys


def addBinary(a, b):
    res = []
    a_idx, b_idx = len(a) - 1, len(b) - 1

    carry = 0
    while a_idx >= 0 or b_idx >= 0 or carry > 0:
        if a_idx >= 0:
            carry += int(a[a_idx])
            a_idx -= 1
        if b_idx >= 0:
            carry += int(b[b_idx])
            b_idx -= 1

        res.append(str(carry % 2))
        carry = carry // 2
    return "".join(reversed(res))


def main():
    a = "11"
    b = "1011"
    print(addBinary(a, b))
    return


if __name__ == "__main__":
    sys.exit(main())
