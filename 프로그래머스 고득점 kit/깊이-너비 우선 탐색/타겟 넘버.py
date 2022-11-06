# bfs 백트래킹 조건 없으니 전부 완탐
from collections import deque, Counter


def solution(numbers, target):
    q = deque([(0, 0)])
    end = []

    while q:
        acc, index = q.popleft()

        if index == len(numbers):
            end.append(acc)
            continue

        q.append((acc + numbers[index], index + 1))
        q.append((acc - numbers[index], index + 1))

    return Counter(end)[target]


print(solution([1, 1, 1, 1, 1],	3) == 5)
print(solution([4, 1, 2, 1], 4) == 2)
