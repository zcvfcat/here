# # 그냥 풀기 통과
# def solution(arr):
#     ans = []
#     k = -1
#     for i in arr:
#         if k == i:
#             continue
#         else:
#             k = i
#             ans.append(k)

#     return ans

# 다른사람 풀이

# 그냥 풀기 통과
def solution(arr):
    ans = []
    for i in arr:
        if ans[-1:] == [i]:
            continue
        ans.append(i)

    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1])
print(solution([4, 4, 4, 3, 3]) == [4, 3])
