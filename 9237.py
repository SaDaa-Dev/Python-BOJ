# 9237 이장님 초대
import sys
n = int(input())
date = list(map(int, input().split()))
date.sort(reverse=True)
index = 1

for i in range(n):
    date[i] += index
    index += 1

print(max(date) + 1)
