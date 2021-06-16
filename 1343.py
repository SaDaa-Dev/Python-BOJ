# 1343번 폴리오미노
import sys

data = sys.stdin.readline().strip()
data = data.replace("XXXX", "AAAA")
data = data.replace("XX", "BB")

if 'X' in data:
    print(-1)
else:
    print(data)
