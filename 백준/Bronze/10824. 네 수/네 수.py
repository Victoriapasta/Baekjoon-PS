import sys
input = sys.stdin.readline

a, b, c, d = map(str, input().split())

newA = int(a + b)
newB = int(c + d)

print(newA + newB)