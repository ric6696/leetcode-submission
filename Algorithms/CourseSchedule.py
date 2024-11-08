import sys


def CourseSchedule(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for x, y in prerequisites:
        graph[x].append(y)
    visited = []

    def dfs(x):
        if x in visited:
            return False
        elif graph[x] == []:
            return True
        visited.append(x)
        for y in graph[x]:
            if not dfs(y):
                return False
        visited.remove(x)
        graph[x] = []
        print(visited)
        return True

    for x in range(numCourses):
        if not dfs(x):
            return False
    return True


def main():
    numCourses = 5
    prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    print(CourseSchedule(numCourses, prerequisites))


if __name__ == "__main__":
    sys.exit(main())
