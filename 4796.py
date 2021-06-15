# 4796 캠핑
import sys

i = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l+p+v == 0:
        break

    rest = (v//p)*l
    rest += min((v % p), l)
    print("Case {0}: {1}".format(i, rest))
    i += 1
