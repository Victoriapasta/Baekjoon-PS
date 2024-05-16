n, m = map(int, input().split())

arr = list(map(int, input().split()))

answer = []

for num in arr:
    answer.append(num - n * m)


print(*answer)