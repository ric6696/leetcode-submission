import heapq
import sys


def findAnswer(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    print(graph)

    def dijkstra(graph, source):
        dist = {i: float("inf") for i in range(len(graph))}

        min_heap = [(0, source)]

        while min_heap:
            cur_dist, cur_node = heapq.heappop(min_heap)

            if cur_dist < dist[cur_node]:
                dist[cur_node] = cur_dist

                for n, w in graph[cur_node]:
                    new_dist = cur_dist + w
                    heapq.heappush(min_heap, (new_dist, n))
        return dist

    dist1 = dijkstra(graph, 0)
    dist2 = dijkstra(graph, n - 1)
    total = dist2[0]

    if total == float("inf"):
        return [False] * len(edges)
    return [
        (dist1[v1] + w + dist2[v2] == total) or (dist1[v2] + w + dist2[v1] == total)
        for (v1, v2, w) in edges
    ]


def main():
    n = 6
    edges = [
        [0, 1, 4],
        [0, 2, 1],
        [1, 3, 2],
        [1, 4, 3],
        [1, 5, 1],
        [2, 3, 1],
        [3, 5, 3],
        [4, 5, 2],
    ]
    print(findAnswer(n, edges))


if __name__ == "__main__":
    sys.exit(main())
