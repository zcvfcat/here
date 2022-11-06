# 늦어서 자러감... 자기전에 답보고
# 그리고 어려움... ㅠㅜ
# 공부한 자료 https://osnim.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%85%EA%B5%AD-%EC%8B%AC%EC%82%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(n, times):
    answer = 0
    start = 1
    # 최악의 경우: 가장 오래 걸리는 심사위원에게 모두 심사 받는 경우
    end = max(times) * n
    while start <= end:
        people = 0  # 입국 심사 완료된 사람 수
        mid = (start + end) // 2  # mid 시간 동안 입국심사가 가능한지 판단
        for time in times:
            # 입국 심사가 가능한 사람 수
            people += mid//time

        # n 이상 심사 = mid로 가능하지만 더 가능할 수 있으니
        # 일단 answer 에 저장하고 최소 mid 분 찾기
        if people >= n:
            answer = mid
            end = mid - 1
        # n보다 적은 수 심사 = mid으로는 부족
        else:
            start = mid + 1
    return answer


print(solution(6, [7, 10]) == 28)
