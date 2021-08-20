A = 2
B = 162
cnt = 1

while True:
    if str(B)[-1] == '1':
        B = int(str(B)[:-1])
    if B % 2 == 0:
        B = B/2
    print(B)
    cnt += 1

print(cnt)
