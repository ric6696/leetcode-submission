import sys


def captureForts(forts):
    max, i = 0, 0
    while i < len(forts):
        if forts[i] != 0:
            j = i + 1
            while j < len(forts):
                if forts[i] + forts[j] == 0:
                    if j - i - 1 >= max:
                        max = j - i - 1
                    break
                elif forts[i] == forts[j]:
                    break
                j += 1
            i = j
        else:
            i += 1
    return max


def main():
    forts = [1, -1, -1, 1, 1]
    print(captureForts(forts))


if __name__ == "__main__":
    sys.exit(main())
