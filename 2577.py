# 2577 숫자의 개수
data = [int(input()) for _ in range(3)]
mul = 1
cnt = 0
for i in range(len(data)):
    mul *= data[i]
re = list(map(int, str(mul)))
for i in range(10):
    cnt = 0
    for j in re:
        if i == j:
            cnt += 1
    print(cnt)
