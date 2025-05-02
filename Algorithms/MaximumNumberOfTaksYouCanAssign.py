import sys
import bisect


def maxTaskAssign(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()

    print("sorted tasks: ", tasks)
    print("sorted workers: ", workers)
    left, right = 0, min(len(tasks), len(workers))
    it = 0

    while left < right:
        print("\n")
        print(f"iteration {it}")
        print(f"left: {left}", f"right: {right}")
        mid = (left + right + 1) // 2
        usedPills = 0
        availWorkers = workers[-mid:]
        canAssign = True
        print("available workers =", availWorkers)

        for t in reversed(tasks[:mid]):
            print("t =", t)
            print("availWorkers[-1]: ", availWorkers[-1])
            if availWorkers[-1] >= t:
                availWorkers.pop()
            else:
                idx = bisect.bisect_left(availWorkers, t - strength)
                print(f"index: {idx}")
                if idx == len(availWorkers) or usedPills == pills:
                    canAssign = False
                    break
                usedPills += 1
                availWorkers.pop(idx)
            print("available workers for loop =", availWorkers)

        if canAssign == True:
            left = mid
        else:
            right = mid - 1
        it += 1

    return left


def main():
    tasks = [5, 9, 8, 5, 9]
    workers = [1, 6, 4, 2, 6]
    pills = 1
    strength = 5

    print(maxTaskAssign(tasks, workers, pills, strength))


if __name__ == "__main__":
    sys.exit(main())
