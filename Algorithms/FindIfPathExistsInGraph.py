import sys


def validPath(n, edges, source, destination):
    graph = {i: [] for i in range(0, n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = [source]
    visited = set()

    while queue:
        cur_node = queue.pop(0)
        if cur_node == destination:
            return True
        if cur_node in visited:
            continue
        visited.add(cur_node)
        for w in graph[cur_node]:
            if w not in visited:
                queue.append(w)

    return False


def main():
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    print(validPath(n, edges, source, destination))


if __name__ == "__main__":
    sys.exit(main())
