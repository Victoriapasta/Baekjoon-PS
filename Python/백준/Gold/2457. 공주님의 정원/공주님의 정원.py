import sys

input = sys.stdin.readline

n = int(input())

days = []
for _ in range(n):
    days.append(list(map(int, input().split())))

days.sort()

cnt = 0
temp = (3, 1)

for i in range(len(days)):
    if (days[i][0], days[i][1]) <= temp < (days[i][2], days[i][3]):
        temp2 = (days[i][2], days[i][3])
        for j in range(i, len(days) - 1):
            if temp < (days[j + 1][0], days[j + 1][1]):
                break
            if temp2 < (days[j + 1][2], days[j + 1][3]):
                temp2 = (days[j + 1][2], days[j + 1][3])

        cnt += 1
        temp = temp2

    if (11, 30) < temp:
        print(cnt)
        exit(0)

print(0)
