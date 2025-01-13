import sys


def isValid(s):
    stack = []
    openBrac = {"(": ")", "{": "}", "[": "]"}
    closeBrac = [")", "}", "]"]

    for char in s:
        if char in openBrac:
            stack.append(char)
        if char in closeBrac:
            if not stack:
                return False
            element = stack.pop()
            if openBrac[element] != char:
                return False

    if stack:
        return False
    return True


def main():
    s = "()[]{}"
    print(isValid(s))


if __name__ == "__main__":
    sys.exit(main())
