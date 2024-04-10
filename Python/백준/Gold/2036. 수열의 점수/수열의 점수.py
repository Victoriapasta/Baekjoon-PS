import sys
input = sys.stdin.readline

n = int(input())

positive = []
negative = []

answer = 0
for i in range(n):
    temp = int(input())
    if temp > 1:
        positive.append(temp)
    elif temp == 1:
        answer += 1
    else:
        negative.append(temp)

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i + 1 >= len(positive):
        answer += positive[i]
        continue
    answer += positive[i] * positive[i + 1]

for i in range(0, len(negative), 2):
    if i + 1 >= len(negative):
        answer += negative[i]
        continue
    answer += negative[i] * negative[i + 1]

print(answer)