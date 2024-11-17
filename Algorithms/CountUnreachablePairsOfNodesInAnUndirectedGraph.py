import sys
from collections import deque


def countPairs(n, edges):
    graph = {i: [] for i in range(0, n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    unvisited = set(range(0, n))
    queue = deque()
    res, cnt = 0, 0

    while unvisited:
        print(unvisited)
        print(queue)
        if not queue:
            res += cnt * (len(unvisited))
            queue.append(unvisited.pop())
            cnt = 0
        print(res, cnt)
        cur_node = queue.popleft()  # dequeue the next node
        for w in graph[cur_node]:
            if w in unvisited:
                queue.append(w)
                unvisited.remove(w)
        cnt += 1
    return res


def main():
    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    print(countPairs(n, edges))


if "__main__" == __name__:
    sys.exit(main())
