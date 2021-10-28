# 5622 다이얼
import sys
dials = ['ABC', 'DEF', 'GHI', "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
dial = sys.stdin.readline().rstrip()
re = 0
for i in dial:
    for j in dials:
        if i in j:
            re += dials.index(j) + 3
print(re)
