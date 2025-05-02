import sys


def pushDominoes(dominoes):
    dom = list(dominoes)
    left = 0
    for right in range(len(dom)):
        if dom[right] == "L":
            while left < right:
                if dom[left] == ".":
                    dom[left] = "L"
                    left += 1
                if dom[left] == "L":
                    for k in range(left + 1, right):
                        dom[k] = "L"
                    break
                if dom[left] == "R":
                    length = right - left - 1
                    for k in range(1, length // 2 + 1):
                        dom[left + k] = "R"
                        dom[right - k] = "L"
                    left = right

        elif dom[right] == "R":
            if dom[left] == "R":
                for k in range(left + 1, right):
                    dom[k] = "R"
            left = right

    if dom[left] == "R":
        for k in range(left, len(dom)):
            dom[k] = "R"

    return dom


def main():
    dominoes = ".L.R...LR..L.."
    dominoe2 = "L.LL......"
    print(pushDominoes(dominoes))
    print(pushDominoes(dominoe2))


if __name__ == "__main__":
    sys.exit(main())


# .L -> LL
# L. -> L.
# .R -> .R
# R. -> RR

# LR -> LR

# RL ->
# even -> RL
# odd -> R.L
