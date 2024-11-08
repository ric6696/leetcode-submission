import sys


def isBipartite(graph):
    """The time complexity should be O(n+m) use BFS to solve this problem"""
    n = len(graph)
    colors = [None] * n
    for i in range(n):
        if colors[i] is None:
            colors[i] = 1
            queue = [i]
            while queue:
                currentNode = queue.pop(0)
                for node in graph[currentNode]:
                    if colors[node] is None:
                        colors[node] = 1 - colors[currentNode]
                        queue.append(node)
                    elif colors[node] == colors[currentNode]:
                        return False

    return True


def main():
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(isBipartite(graph))


if __name__ == "__main__":
    sys.exit(main())
