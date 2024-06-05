import math
import sys

input = sys.stdin.readline

INF = 1000001
arr = [i for i in range(INF)]


def eratosthenes():
    global arr
    for i in range(2, int(math.sqrt(INF)) + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, INF, i):
            arr[j] = 0


def goldbach(n):
    global arr
    for i in range(2, n):
        if arr[i] == i:
            temp = n - i
            if arr[temp] == temp:
                return i, temp

    return -1, -1


if __name__ == '__main__':
    eratosthenes()
    while True:
        n = int(input())
        if n == 0:
            break
        a, b = goldbach(n)
        if a == -1 and b == -1:
            print("Goldbach's conjecture is wrong.")
        else:
            print("%d = %d + %d" % (n, a, b))
