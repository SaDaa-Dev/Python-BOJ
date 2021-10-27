import sys
target = sys.stdin.readline().rstrip().upper()
re = []
reStr = []
while True:
    re.append(target.count(target[0]))
    reStr.append(target[0])
    target = target.replace(target[0], "")
    if len(target) < 1:
        break

if re.count(max(re)) > 1:
    print("?")
else:
    print(reStr[re.index(max(re))])
