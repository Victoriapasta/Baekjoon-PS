import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    answer = 0
    maxPrice = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > maxPrice:
            maxPrice = arr[i]
        else:
            answer += maxPrice - arr[i]

    print(answer)
