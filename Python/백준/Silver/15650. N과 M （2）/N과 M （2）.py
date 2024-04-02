from itertools import combinations

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

answer = combinations(arr, m)

for nums in answer:
    print(*nums)