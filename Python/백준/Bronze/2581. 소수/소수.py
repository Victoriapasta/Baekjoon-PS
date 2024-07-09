import math

m = int(input())
n = int(input())
arr = [i for i in range(n + 1)]


def eratosthenes(n):
    end = int(math.sqrt(n))
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, n + 1, i):
            arr[j] = 0


arr[1] = 0
eratosthenes(n)
answer = 0
minn = -1
for i in range(m, n + 1):
    if arr[i] != 0:
        if minn == -1:
            minn = arr[i]
        answer += arr[i]

if answer:
    print(answer)
    print(minn)
else:
    print(-1)
