import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cons = True
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(str(input().rstrip()))

    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1][:len(arr[i])]:
            cons = False
            break

    if cons:
        print('YES')
    else:
        print('NO')