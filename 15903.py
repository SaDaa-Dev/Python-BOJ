# 15903 카드 합체 놀이
import sys

n, m = map(int, input().split())
data = list(map(int, input().split()))
for _ in range(m):
    data.sort()
    cardsum = data[0] + data[1]
    data[0], data[1] = cardsum, cardsum

print(sum(data))
