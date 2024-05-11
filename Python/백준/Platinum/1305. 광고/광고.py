import sys
input = sys.stdin.readline

n = int(input())

st = str(input().rstrip())

arr = [0] * len(st)
temp = 0

for i in range(1, len(st)):
    while temp > 0 and st[i] != st[temp]:
        temp = arr[temp - 1]

    if st[i] == st[temp]:
        temp += 1
        arr[i] = temp

print(n - arr[-1])