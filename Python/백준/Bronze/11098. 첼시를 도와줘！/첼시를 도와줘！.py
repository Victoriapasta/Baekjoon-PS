import sys

input = sys.stdin.readline


def find(n):
    has = {}
    for i in range(n):
        a, b = input().split()
        has[int(a)] = b

    print(has[max(has.keys())])


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        find(int(input()))
