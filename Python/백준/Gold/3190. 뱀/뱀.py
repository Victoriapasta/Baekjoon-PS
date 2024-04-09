import sys
from collections import deque

input = sys.stdin.readline

currentTime = 0
currentSnakeLen = deque([(0, 0)])
currentSnake = [0, 0]  # currentSnake[0]은 x 좌표, currentSnake[1]은 y 좌표
nowDirect = 0

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for __ in range(n)]
visited = [[False for _ in range(n)] for __ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1  # 사과의 위치 기록

l = int(input())

for _ in range(l):
    X, C = map(str, input().split())
    X = int(X)

    while True:
        currentTime += 1

        if nowDirect % 4 == 0:  # 오른쪽 방향
            currentSnake[1] += 1
            currentSnakeLen.append([currentSnake[0], currentSnake[1]])
        if nowDirect % 4 == 1:  # 아래 방향
            currentSnake[0] += 1
            currentSnakeLen.append([currentSnake[0], currentSnake[1]])
        if nowDirect % 4 == 2:  # 왼쪽 방향
            currentSnake[1] -= 1
            currentSnakeLen.append([currentSnake[0], currentSnake[1]])
        if nowDirect % 4 == 3:  # 위쪽 방향
            currentSnake[0] -= 1
            currentSnakeLen.append([currentSnake[0], currentSnake[1]])

        if n <= currentSnake[0] or currentSnake[0] < 0 or n <= currentSnake[1] or currentSnake[1] < 0:
            print(currentTime)
            exit(0)

        if visited[currentSnake[0]][currentSnake[1]]:  # 방문처리가 된 곳은 지금 몸통이 있는 곳
            print(currentTime)
            exit(0)

        visited[currentSnake[0]][currentSnake[1]] = True

        if board[currentSnake[0]][currentSnake[1]] == 1:  # 사과일때
            board[currentSnake[0]][currentSnake[1]] = 0
        else:
            tempX, tempY = currentSnakeLen.popleft()  # 꼬리 줄이는 로직
            visited[tempX][tempY] = False

        if currentTime == X:
            break

    if C == 'D':
        nowDirect += 1
    if C == 'L':
        if nowDirect == 0:
            nowDirect = 3
        else:
            nowDirect -= 1

while True:
    currentTime += 1

    if nowDirect % 4 == 0:  # 오른쪽 방향
        currentSnake[1] += 1
        currentSnakeLen.append([currentSnake[0], currentSnake[1]])
    if nowDirect % 4 == 1:  # 아래 방향
        currentSnake[0] += 1
        currentSnakeLen.append([currentSnake[0], currentSnake[1]])
    if nowDirect % 4 == 2:  # 왼쪽 방향
        currentSnake[1] -= 1
        currentSnakeLen.append([currentSnake[0], currentSnake[1]])
    if nowDirect % 4 == 3:  # 위쪽 방향
        currentSnake[0] -= 1
        currentSnakeLen.append([currentSnake[0], currentSnake[1]])

    if n <= currentSnake[0] or currentSnake[0] < 0 or n <= currentSnake[1] or currentSnake[1] < 0:
        print(currentTime)
        exit(0)

    if visited[currentSnake[0]][currentSnake[1]]:  # 방문처리가 된 곳은 지금 몸통이 있는 곳
        print(currentTime)
        exit(0)

    visited[currentSnake[0]][currentSnake[1]] = True

    if board[currentSnake[0]][currentSnake[1]] == 1:  # 사과일때
        board[currentSnake[0]][currentSnake[1]] = 0
    else:
        tempX, tempY = currentSnakeLen.popleft()  # 꼬리 줄이는 로직
        visited[tempX][tempY] = False

    if currentTime == X:
        break