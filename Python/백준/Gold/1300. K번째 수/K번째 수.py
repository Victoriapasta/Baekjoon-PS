import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

answer = 0


def binary_search(start, end):
    global answer

    if start > end:
        return answer

    mid = (start + end) // 2

    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, mid // i)

    if cnt >= k:
        answer = mid
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


print(binary_search(1, k))
