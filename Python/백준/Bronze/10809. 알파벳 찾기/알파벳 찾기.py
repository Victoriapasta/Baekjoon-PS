n = str(input().rstrip())
alph = 'abcdefghijklmnopqrstuvwxyz'
dc = {}
for i in alph:
    dc[i] = -1

for i in range(len(n)):
    if dc[n[i]] >= 0:
        continue
    dc[n[i]] = i

arr = list(dc.values())
print(*arr)