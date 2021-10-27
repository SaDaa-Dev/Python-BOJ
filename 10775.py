# 10775 공항
import sys
gate = int(sys.stdin.readline())
plane = int(sys.stdin.readline())
data = list(int(input()) for _ in range(plane))
data.sort()
re = []
for i in range(plane):
    if data[i] > i:
        re.append(data[i])
print(len(re))
