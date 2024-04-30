import sys

input = sys.stdin.readline
INF = int(10 ** 9)
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

chickens, homes = [], []
road = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append([i, j])
        if graph[i][j] == 1:
            homes.append([i, j])

answer = INF


def backTracking(a, count):
    global answer
    global chickens
    global homes

    if a > len(chickens):
        return

    if count == m:
        totalDistance = 0
        for x, y in homes:
            distance = INF
            for i in road:
                nx, ny = chickens[i]
                distance = min(distance, abs(nx - x) + abs(ny - y))
            totalDistance += distance
        answer = min(answer, totalDistance)
        return

    road.append(a)
    backTracking(a + 1, count + 1)
    road.pop()
    backTracking(a + 1, count)


backTracking(0, 0)
print(answer)