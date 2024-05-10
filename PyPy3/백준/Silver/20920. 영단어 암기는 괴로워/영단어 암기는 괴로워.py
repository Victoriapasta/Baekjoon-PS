import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = {}

for i in range(n):
    temp = str(input().rstrip())
    if len(temp) < m:
        continue

    if temp in arr:
        arr[temp] += 1
    else:
        arr[temp] = 1

ans = list(arr.keys())
ans.sort(key=lambda x: (-arr[x], -len(x), x))

for i in ans:
    print(i)