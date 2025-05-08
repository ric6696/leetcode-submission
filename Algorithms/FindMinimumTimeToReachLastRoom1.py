import sys
import heapq


def minTimeToReach(moveTime):
    n = len(moveTime)
    m = len(moveTime[0])
    dist = [[float("inf")] * m for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    minh = []
    heapq.heappush(minh, (0, 0, 0))
    moveTime[0][0] = 0

    while minh:
        t, row, col = heapq.heappop(minh)
        if row == n - 1 and col == m - 1:
            return t
        dist[row][col] = t
        for dx, dy in dir:
            nextRow = row + dy
            nextCol = col + dx
            if (
                nextRow < 0
                or nextRow > n - 1
                or nextCol < 0
                or nextCol > m - 1
                or dist[nextRow][nextCol] != float("inf")
            ):
                continue
            nextT = max(t, moveTime[nextRow][nextCol]) + 1
            heapq.heappush(minh, (nextT, nextRow, nextCol))

    return -1


def main():
    moveTime = [[0, 8], [4, 6]]
    print(minTimeToReach(moveTime))


if __name__ == "__main__":
    sys.exit(main())
