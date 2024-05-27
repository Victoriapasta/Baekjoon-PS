n = str(input().rstrip())
temp = []

if not '0' in n:
    print(-1)
    exit(0)

for i in n:
    temp.append(int(i))

if sum(temp) % 3:
    print(-1)
    exit(0)


print(''.join(sorted(n, reverse=True)))
