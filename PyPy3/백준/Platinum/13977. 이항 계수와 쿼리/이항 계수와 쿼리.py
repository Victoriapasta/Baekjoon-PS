import sys

input = sys.stdin.readline

p = 1000000007
fact = [1] * 4000001
for i in range(2, 4000001):
    fact[i] = (fact[i - 1] * i) % p


def sqr(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    temp = sqr(n, k // 2)
    if k % 2:
        return temp * temp * n % p
    else:
        return temp * temp % p


if __name__ == '__main__':
    m = int(input())
    for _ in range(m):
        n, k = map(int, input().split())

        top = fact[n]
        bottom = fact[n - k] * fact[k] % p

        print(top * sqr(bottom, p - 2) % p)
