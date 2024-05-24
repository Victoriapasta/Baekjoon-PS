n, k = map(int, input().split())

arr = [i for i in range(1, n + 1) if not n % i]

if len(arr) >= k:
    print(arr[k - 1])
else:
    print(0)