n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

answer = 0

for i in range(n - 1, 0, -1):
    while arr[i] <= arr[i - 1]:
        arr[i - 1] -= 1
        answer += 1

print(answer)
