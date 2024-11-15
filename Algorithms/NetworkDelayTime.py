import heapq
import sys


def networkDelayTime(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {node: float("inf") for node in range(1, n + 1)}
    dist[k] = 0

    min_heap = [(0, k)]  # (distance, node)

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(min_heap, (new_dist, v))
            print(min_heap)
    print(dist)
    max_dist = max(dist.values())
    return max_dist if max_dist < float("inf") else -1

    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {node: float("inf") for node in range(1, n + 1)}
    dist[k] = 0

    min_heap = [(0, k)]

    while min_heap:
        cur_dist, u = heapq.heappop(min_heap)
        for v, w in graph[u]:
            dist[v] = min(dist[v], cur_dist + w)
            heapq.heappush(min_heap, (dist[v], v))
            print(min_heap)

    if max(dist.values()) == float("inf"):
        return -1
    return max(dist.values())


def main():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    print(networkDelayTime(times, N, K))


if __name__ == "__main__":
    sys.exit(main())
