import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


def divide_and_conquer(A, B):
    if B == 1:
        return A % c

    if B % 2 == 0:
        return divide_and_conquer(A, B // 2) ** 2 % c
    else:
        return divide_and_conquer(A, B // 2) ** 2 * a % c


print(divide_and_conquer(a, b))
