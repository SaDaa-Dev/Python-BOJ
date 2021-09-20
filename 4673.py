# 4673 셀프 넘버
bfNum = set(range(1, 10001))
afNum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    afNum.add(i)
self_num = sorted(bfNum - afNum)
for i in self_num:
    print(i)
