# 13305 주유소
import sys
n = int(sys.stdin.readline().strip())
streets = list(map(int, sys.stdin.readline().strip().split()))
oilcost = list(map(int, sys.stdin.readline().strip().split()))
re = streets[0] * oilcost[0]
saveP = oilcost[0]  # saveP => 기름값이 더 싼 곳 위치를 저장
for i in range(1, n-1):
    if oilcost[i] < saveP:
        saveP = oilcost[i]
    re += saveP*streets[i]
print(re)
