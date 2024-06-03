p = 1000000007

def fact(n):
    fac = 1
    for i in range(2, n + 1):
        fac = (fac * i) % p
    return fac


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
    n, k = map(int, input().split())

    top = fact(n)
    bottom = fact(n - k) * fact(k) % p

    print(top * sqr(bottom, p - 2) % p)
