# 2884 ěëěęł
h, m = map(int, input().split())
afm = m - 45

if afm < 0:
    afh = h - 1
    if afh < 0:
        afh = 23
    print("{0} {1}".format(afh, 60+afm))
else:
    print("{0} {1}".format(h, afm))
