# 첫번째만 맞음 ㅠㅜ 시도 후 다른 사람 풀이
# import heapq

# def solution(scoville, K):
#     heapq.heapify(scoville)
#     cnt = 1

#     while True:
#         end = heapq.heappop(scoville)
#         prevEnd = heapq.heappop(scoville)
#         calced = end + prevEnd*2

#         if calced >= K:
#             return cnt
#         else:
#             cnt += 1
#             heapq.heappush(scoville, calced)
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break

        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        cnt += 1

    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
