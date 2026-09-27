n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start1, start2 = map(int, input().split())
destination = int(input())


def find_paths(start):

    paths = []

    def dfs(current, visited, path):

        if current == destination:
            paths.append(path[:])
            return

        for next_town in graph[current]:

            if next_town not in visited:

                visited.add(next_town)
                path.append(next_town)

                dfs(next_town, visited, path)

                path.pop()
                visited.remove(next_town)

    visited = {start}
    dfs(start, visited, [start])

    return paths


paths1 = find_paths(start1)
paths2 = find_paths(start2)

answer = 999999

for path1 in paths1:

    set1 = set(path1)

    for path2 in paths2:

        set2 = set(path2)

        common = set1 & set2

        if common == {destination}:

            total = len(set1 | set2)

            if total < answer:
                answer = total


if answer == 999999:
    print("Impossible")
else:
    print(answer)
