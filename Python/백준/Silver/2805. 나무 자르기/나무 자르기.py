import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_size = max(arr)
answer = 0


def binary_search(lower, upper):
    if lower > upper:
        return
    global answer

    mid = (lower + upper) // 2
    temp = 0

    for length in arr:
        if length >= mid:
            temp += length - mid

    if temp >= m:
        answer = mid
        binary_search(mid + 1, upper)
    else:
        binary_search(lower, mid - 1)


binary_search(0, max_size * 2)
print(answer)