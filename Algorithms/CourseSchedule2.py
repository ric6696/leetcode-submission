import collections
import sys

# class Solution(object):
# def findOrder(self, numCourses, prerequisites):
#     self.graph = collections.defaultdict(list)
#     self.res = []

#     for cre, pre in prerequisites:
#         self.graph[cre].append(pre)
#     self.visited = [0 for x in range((numCourses))]

#     for x in range(numCourses):
#         if not self.cycle(x):
#             return []

#     return self.res

# def cycle(self, node):
#     if self.visited[node] == -1:  # cycle detected return False
#         return False
#     if self.visited[node] == 1:
#         return True  # has been finished, and been added to self.res
#     self.visited[node] = -1  # mark as visited
#     for _node in self.graph[node]:
#         if not self.cycle(_node):
#             return False
#     self.visited[node] = 1  # mark as finished
#     # add to solution as the course depenedent on previous ones
#     self.res.append(node)
#     return True


def findOrder(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        graph[crs].append(pre)
    output = []
    visited, cycle = set(), set()

    def dfs(node):
        if node in cycle:
            return False
        if node in visited:
            return True

        cycle.add(node)
        for pre in graph[node]:
            if dfs(pre) is False:
                return False
        cycle.remove(node)
        visited.add(node)
        output.append(node)
        return True

    for x in range(numCourses):
        if dfs(x) is False:
            return []

    return output


def main():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    # solution = Solution()
    # print(solution.findOrder(numCourses, prerequisites))
    print(findOrder(numCourses, prerequisites))


if __name__ == "__main__":
    sys.exit(main())
