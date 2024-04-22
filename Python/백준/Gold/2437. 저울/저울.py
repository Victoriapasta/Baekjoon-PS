import sys
input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))

answer = 1

for i in arr:
    if i > answer:
        break
    answer += i

print(answer)