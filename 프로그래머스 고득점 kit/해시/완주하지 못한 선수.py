# 1회차 순수하게 품
# def solution(participant, completion):
#     cp = {}

#     for p in participant:
#         if cp.get(p) is None:
#             cp[p] = 1
#         else:
#             cp[p] += 1

#     for p in completion:
#         if cp[p] > 0:
#             cp[p] -= 1

#     for person, cnt in cp.items():
#         if cnt > 0:
#             return person

# 다른 사람 풀이 Counter 객체 사용
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]) == "leo")
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]) == "vinko")
print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]) == "mislav")
