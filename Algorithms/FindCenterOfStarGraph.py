import sys


def findCenter(edges):
    graph = {i: [] for i in range(1, len(edges) + 2)}
    for v, w in edges:
        graph[v].append(w)
        graph[w].append(v)

    for j in range(1, len(edges) + 2):
        if len(graph[j]) == len(edges):
            return j

    # Simple Solution
    # so this code checks if there are any of the first edges array [0][0] in the second part either first array [] or second array [] of the edges
    # if theres none it wil automatically return the second value of the edges [0][1]
    # return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


def main():
    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(findCenter(edges))


if "__main__" == __name__:
    sys.exit(main())
