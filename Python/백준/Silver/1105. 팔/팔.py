l, r = map(str, input().split())

cnt = 0

if len(l) != len(r):
    print(0)
    exit(0)

for i in range(len(l)):
    if l[i] != r[i]:
        break
    if l[i] == '8':
        cnt += 1

print(cnt)