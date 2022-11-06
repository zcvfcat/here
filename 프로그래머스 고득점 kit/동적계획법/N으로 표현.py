# bfs로 모두 완탐하는데 틀리네;;
# 이건 다이나믹으로 풀어야하는데 모르겠누...
# 다른 사람도 틀림;;
from collections import deque


def solution(N, number):
    q = deque([(N, 1)])

    minimum = -1

    while q:
        curr, cnt = q.popleft()

        if curr == number and minimum == -1:
            minimum = cnt

        if cnt > 8:
            continue

        q.append((int(str(curr) + str(N)), cnt+1))
        q.append((curr + N, cnt+1))
        q.append((curr - N, cnt+1))
        q.append((curr * N, cnt+1))
        q.append((curr // N, cnt+1))

    return minimum


print(solution(5, 12) == 4)
print(solution(2, 11) == 3)
