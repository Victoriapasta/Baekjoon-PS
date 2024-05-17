import sys
input = sys.stdin.readline

channel = int(input().rstrip())
n = int(input())
wrongs = list(map(int, input().split()))

answer = abs(100 - channel)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) in wrongs:
            break

        elif i == len(num) - 1:
            answer = min(answer, abs(int(num) - channel) + len(num))

print(answer)
