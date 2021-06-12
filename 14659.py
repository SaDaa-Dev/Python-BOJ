# 14659 한조서열정리하고옴ㅋㅋ

n = int(input())
data = list(map(int, input().split()))
kill_archer = [0] * (n)
for i in range(n):
    for j in range(i+1, n):
        if (data[i] < data[j]) or (data[i] == data[-1]):
            break
        kill_archer[i] += 1

print(max(kill_archer))
