import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

graph = []
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))


def moveLeft(new_graph):
    for i in range(n):
        dir = 0
        for j in range(1, n):
            if new_graph[i][j] != 0:
                temp = new_graph[i][j]
                new_graph[i][j] = 0

                if new_graph[i][dir] == 0:
                    new_graph[i][dir] = temp
                elif new_graph[i][dir] == temp:
                    new_graph[i][dir] *= 2
                    dir += 1
                else:
                    dir += 1
                    new_graph[i][dir] = temp  # 같은값이 아니면 합쳐지지 않고 옆에 붙어만 있음

    return new_graph


def moveRight(new_graph):
    for i in range(n):
        dir = n - 1
        for j in range(n - 1, -1, -1):
            if new_graph[i][j] != 0:
                temp = new_graph[i][j]
                new_graph[i][j] = 0

                if new_graph[i][dir] == 0:
                    new_graph[i][dir] = temp
                elif new_graph[i][dir] == temp:
                    new_graph[i][dir] *= 2
                    dir -= 1
                else:
                    dir -= 1
                    new_graph[i][dir] = temp

    return new_graph


def moveUp(new_graph):
    for j in range(n):
        dir = 0
        for i in range(n):
            if new_graph[i][j] != 0:
                temp = new_graph[i][j]
                new_graph[i][j] = 0

                if new_graph[dir][j] == 0:
                    new_graph[dir][j] = temp
                elif new_graph[dir][j] == temp:
                    new_graph[dir][j] *= 2
                    dir += 1
                else:
                    dir += 1
                    new_graph[dir][j] = temp

    return new_graph


def moveDown(new_graph):
    for j in range(n):
        dir = n - 1
        for i in range(n - 1, -1, -1):
            if new_graph[i][j] != 0:
                temp = new_graph[i][j]
                new_graph[i][j] = 0

                if new_graph[dir][j] == 0:
                    new_graph[dir][j] = temp
                elif new_graph[dir][j] == temp:
                    new_graph[dir][j] *= 2
                    dir -= 1
                else:
                    dir -= 1
                    new_graph[dir][j] = temp

    return new_graph


def dfs(count, input_graph):
    global answer

    if count == 5:
        for row in input_graph:
            temp = max(row)
            answer = max(answer, temp)

        return

    for i in range(4):
        copy_graph = deepcopy(input_graph)

        if i == 0:
            dfs(count + 1, moveLeft(copy_graph))
        if i == 1:
            dfs(count + 1, moveRight(copy_graph))
        if i == 2:
            dfs(count + 1, moveUp(copy_graph))
        if i == 3:
            dfs(count + 1, moveDown(copy_graph))


dfs(0, graph)
print(answer)
