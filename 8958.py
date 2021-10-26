# 8958번 OX퀴즈
import sys
n = int(sys.stdin.readline().rstrip())
datas = list(sys.stdin.readline().rstrip() for _ in range(n))
for data in datas:
    score = 0
    cnt = 0
    for i in range(len(data)):
        if data[i] == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
