# 10809 알파벳 찾기
target = input()
re = [-1]*26

for unit in target:
    for i in range(ord('a'), ord('z')+1):
        if unit == chr(i):
            re[ord(unit) - ord('a')] = target.index(unit)
print(" ".join(map(str, re)))
