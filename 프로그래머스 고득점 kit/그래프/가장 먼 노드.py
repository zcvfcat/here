# 완탐 문제
from collections import deque, Counter


def solution(n, vertex):
    g = [[] for _ in range(n + 1)]
    for v, e in vertex:
        g[v].append(e)
        g[e].append(v)

    q = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1

    while q:
        curr = q.popleft()

        for next in g[curr]:
            if not visited[next]:
                visited[next] = visited[curr] + 1
                q.append(next)

    m = max(visited)
    return visited.count(m)


print(solution(6, [[3, 6], [4, 3], [3, 2], [
      1, 3], [1, 2], [2, 4], [5, 2]]) == 3)
