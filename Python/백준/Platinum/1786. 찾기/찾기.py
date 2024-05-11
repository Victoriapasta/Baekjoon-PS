import sys

input = sys.stdin.readline

t = str(input().rstrip())
p = str(input().rstrip())

arr = [0] * len(p)
answer = []
temp = 0
temp2 = 0
count = 0

for i in range(1, len(p)):
    while temp > 0 and p[i] != p[temp]:
        temp = arr[temp - 1]

    if p[i] == p[temp]:
        temp += 1
        arr[i] = temp


for i in range(len(t)):
    while temp2 > 0 and t[i] != p[temp2]:
        temp2 = arr[temp2 - 1]

    if t[i] == p[temp2]:
        if temp2 == len(p) - 1:
            answer.append(i - len(p) + 2)
            count += 1
            temp2 = arr[temp2]
        else:
            temp2 += 1


print(count)
print(*answer)
