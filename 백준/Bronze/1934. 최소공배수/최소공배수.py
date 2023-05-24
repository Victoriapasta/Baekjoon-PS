import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    r = a * b
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    print(r//a)