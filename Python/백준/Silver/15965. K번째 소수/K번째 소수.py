import math
import sys

input = sys.stdin.readline

INF = 500001
arr = [i for i in range(INF)]


def eratosthenes():
    global arr
    for i in range(2, int(math.sqrt(INF)) + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, INF, i):
            arr[j] = 0

    return [i for i in arr[2:] if arr[i]]


if __name__ == '__main__':
    primes = eratosthenes()
    print(primes[int(input()) - 1])