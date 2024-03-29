import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maxValue = arr[0]
minValue = arr[0]

for number in arr:
    if number > maxValue:
        maxValue = number
    if number < minValue:
        minValue = number

print(minValue, maxValue)