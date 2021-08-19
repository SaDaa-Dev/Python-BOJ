# 13413 오셀로 재배치
import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    datalen = int(sys.stdin.readline().strip())
    data1 = sys.stdin.readline().strip()
    data2 = sys.stdin.readline().strip()
    cnt = 0
    data_list1 = []
    data_list2 = []

    for i in range(datalen):
        if (data1[i] != data2[i]):
            data_list1.append(data1[i])
            data_list2.append(data2[i])

    data_list1 = sorted(data_list1)
    data_list2 = sorted(data_list2)

    for i in range(len(data_list1)):
        if data_list1[i] == data_list2[i]:
            cnt += 0.5
        else:
            cnt += 1

    print(int(cnt))
