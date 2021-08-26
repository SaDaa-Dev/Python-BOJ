# 1449 수리공 항승
import sys
n, l = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
start, end = data[0], data[0]+l
cnt = 1
for i in range(n):
    if start <= data[i] < end:
        continue
    else:
        start = data[i]
        end = data[i]+l
        cnt += 1
print(cnt)
