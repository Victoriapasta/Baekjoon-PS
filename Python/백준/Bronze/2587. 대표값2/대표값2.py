import sys

input = sys.stdin.readline

arr = []

for i in range(5):
    arr.append(int(input()))

arr.sort()
print(int(sum(arr) / 5))
print(int(arr[2]))
