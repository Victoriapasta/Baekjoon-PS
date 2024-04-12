import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
answer = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        answer[i][j] = answer[i - 1][j] + answer[i][j - 1] - answer[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(answer[x2][y2] - answer[x2][y1 - 1] - answer[x1 - 1][y2] + answer[x1 - 1][y1 - 1])
