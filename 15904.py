# 15904 UCPC는 무엇의 약자일까?
import sys

data = sys.stdin.readline()

check_point = ["U", "C", "P", "C"]
check_flag = True

for i in range(len(check_point)):
    if check_point[i] in data:
        check_flag = True
        idx = data.find(check_point[i])
        data = data[idx+1:]
    else:
        check_flag = False
        break

if check_flag == True:
    print("I love UCPC")
else:
    print("I hate UCPC")
