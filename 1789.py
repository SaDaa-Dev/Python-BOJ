import sys
n = int(sys.stdin.readline())
res = 0
i = 1
while True:
    res += i
    if res > n:
        print(i-1)
        break
    elif res == n:
        print(i)
        break
    i += 1
