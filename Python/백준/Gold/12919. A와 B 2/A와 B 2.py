import sys

input = sys.stdin.readline

s = str(input().rstrip())
T = str(input().rstrip())


def dfs(t):
    global s
    if s == t:
        print(1)
        exit(0)

    if not len(t):
        return
    
    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(T)
print(0)