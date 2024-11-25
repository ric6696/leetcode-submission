import sys


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def Tribonacci(n):
    F = [0] * 38
    F[0], F[1], F[2] = 0, 1, 1

    for i in range(3, n + 1):
        F[i] = F[i - 3] + F[i - 2] + F[i - 1]
    return F[n]


def main():
    n = 25
    print(fibonacci(6))
    print(Tribonacci(n))


if __name__ == "__main__":
    sys.exit(main())
