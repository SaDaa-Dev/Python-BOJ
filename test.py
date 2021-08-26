n = 4
l = 2
data = [1, 2, 100, 101]
data.sort
cnt = 1
start = data[0]
end = data[0] + l
for i in range(n):
    if start <= data[i] < end:
        continue
    else:
        start = data[i]
        end = data[i] + l
        cnt += 1

print(cnt)
