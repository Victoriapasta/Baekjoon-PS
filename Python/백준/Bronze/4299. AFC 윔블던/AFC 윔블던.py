n, m = map(int, input().split())

a = (n + m) / 2
b = (n - m) / 2

arr = [int(a), int(b)]

if a != int(a) or b != int(b) or a < 0 or b < 0:
    print(-1)
else:
    print(*sorted(arr, reverse=True))
