import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [0]

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    elif arr[i] < dp[-1]:
        start, end = 0, len(dp) - 1
        target = arr[i]
        while start < end:
            mid = (start + end) // 2

            if dp[mid] < target:
                start = mid + 1
            else:
                end = mid

        dp[end] = target

print(len(dp) - 1)
