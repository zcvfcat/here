# 1회차 반 맞음... 틀림 ㅠㅠ
# 오른쪽만 생각함 왼쪽도 생각해야함;; lost 2,4 reserve 3,5 일 경우 뒤로 계산 해야함;;
# ??? 다른 사람것도 다 틀림;;
def solution(n, lost, reserve):
    lost = {value: 1 for value in lost}
    reserve = {value: 1 for value in reserve}
    cnt = 0

    for i in range(1, n+1):
        if lost.get(i) is not None:
            if i > 1 and reserve.get(i-1) is not None:
                cnt += 1
                del reserve[i-1]
            elif i < n and reserve.get(i+1) is not None:
                cnt += 1
                del reserve[i+1]
            continue

        cnt += 1

    lost = {value: 1 for value in lost}
    reserve = {value: 1 for value in reserve}
    reverseCnt = 0

    for i in range(n, 0, -1):
        if lost.get(i) is not None:
            if i > 1 and reserve.get(i-1) is not None:
                reverseCnt += 1
                del reserve[i-1]
            elif i < n and reserve.get(i+1) is not None:
                reverseCnt += 1
                del reserve[i+1]
            continue

        reverseCnt += 1

    return max(cnt, reverseCnt)


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(3, [3], [1]) == 2)
