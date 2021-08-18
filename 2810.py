# 2810 컵홀더
import sys
cnt = 0
n = int(sys.stdin.readline().strip())
seat = sys.stdin.readline().strip()
seat = seat.replace("LL", "S")
for i in range(len(seat)-1):
    if seat[i] == seat[i+1]:
        cnt += 1
cnt += 2
if (cnt > n):
    print(n)
else:
    print(cnt)
