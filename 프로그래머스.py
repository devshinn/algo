# 디펜스 게임 문제
# import heapq

# def solution(n, k, enemy):
#     # enemy = [4, 2, 4, 5, 3, 3, 1]

#     minHeap = enemy[:k]  # [2, 4, 4]
#     heapq.heapify(minHeap)
#     print(minHeap)
#     for i in range(k, len(enemy)):
#         heapq.heappush(minHeap, enemy[i])  # push 5 => [2, 4, 4, 5]
#         print(minHeap, i)
#         n -= heapq.heappop(minHeap)

#         if n < 0:
#             return i
#     return len(enemy)


# solution(2, 4, [3, 3, 3, 3])

# 문자열 나누기 문제
from collections import deque


def solution(s):
    s = deque(list(s))
    answer = 0
    while s:
        xCount = 1
        dCount = 0
        x = s.popleft()
        answer += 1

        for i in range(len(s)):

            if x == s.popleft():
                xCount += 1
            else:
                dCount += 1
            print(s, answer, xCount, dCount)
            if xCount == dCount:
                break

    return answer
