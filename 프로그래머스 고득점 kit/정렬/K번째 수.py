# 첫 시도 통과 나쁘지 않은 코드

def solution(array, commands):
    ans = []
    for i, j, k in commands:
        target = sorted(array[i - 1:j])
        ans.append(target[k - 1])

    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [
      [2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3])
