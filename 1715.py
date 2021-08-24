# 1715번 카드 정렬하기
import heapq
n = int(input())
data = list(int(input()) for i in range(n))
heapq.heapify(data)
re = 0

while len(data) > 1:
    num1 = heapq.heappop(data)
    num2 = heapq.heappop(data)
    saveN = num1 + num2
    re += saveN
    heapq.heappush(data, saveN)

print(re)
