# 1110 더하기 싸이클
import sys
bfNum = int(sys.stdin.readline().rstrip())
cnt = 0

temp = 0
newNum = 0
reNum = bfNum
while True:
    temp = (bfNum//10) + (bfNum % 10)
    newNum = (bfNum % 10) * 10 + (temp % 10)
    bfNum = newNum
    cnt += 1
    if bfNum == reNum:
        break
print(cnt)
