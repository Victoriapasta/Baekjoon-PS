import sys
input = sys.stdin.readline

arr = sorted(list(map(int, input().split())))
ans = 0
if arr[2] == arr[0]:
    ans = 10000 + arr[0] * 1000
elif arr[2] == arr[1] or arr[1] == arr[0]:
    ans = 1000 + arr[1] * 100
else:
    ans = 100 * arr[2]

print(ans)