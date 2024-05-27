a, b = map(str, input().split())
cnt = 1
while int(b) >= int(a):

    if not int(b) % 2:
        b = int(b) // 2
        cnt += 1
    elif str(b)[-1] == '1':
        b = str(b)[:-1]
        cnt += 1
    else:
        print(-1)
        exit(0)

    if int(b) == int(a):
        print(cnt)
        exit(0)

print(-1)