import math
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    sqRoot = math.floor(math.sqrt(dist))
    sq = sqRoot * sqRoot

    if dist <= 3:
        print(dist)
        continue

    if dist == sq:
        print(sqRoot + sqRoot - 1)
        continue

    if sq + sqRoot < dist:
        print(sqRoot + sqRoot + 1)
        continue

    if sq < dist <= sq + sqRoot:
        print(sqRoot + sqRoot)
        continue
