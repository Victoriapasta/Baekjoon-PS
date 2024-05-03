import sys

input = sys.stdin.readline

n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

answer = {}

for i in arr2:
    answer[i] = 0

for i in arr1:
    if i in answer:
        answer[i] += 1

print(*answer.values())