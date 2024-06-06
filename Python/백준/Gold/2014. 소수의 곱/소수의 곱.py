import sys
import heapq

input = sys.stdin.readline


def primeProduct(arr, m):
    for i in range(m):
        number, baseidx = heapq.heappop(arr)

        for idx, prime in enumerate(primes):
            if idx > baseidx:
                break

            temp = prime * number
            heapq.heappush(arr, (temp, idx))

        if i == m - 1:
            return number


if __name__ == '__main__':
    k, n = map(int, input().split())
    primes = list(map(int, input().split()))
    heap = []

    for index, prime in enumerate(primes):
        heapq.heappush(heap, (prime, index))

    print(primeProduct(heap, n))
