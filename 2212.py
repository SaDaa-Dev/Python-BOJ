# 2212 센서
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sen = list(map(int, sys.stdin.readline().split()))
sen.sort()

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(sen[i] - sen[i-1])

dist.sort()
for _ in range(k-1):
    dist.pop()

print(sum(dist))
