import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
length = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            length[i] = max(length[i], length[j] + 1)

print(max(length))