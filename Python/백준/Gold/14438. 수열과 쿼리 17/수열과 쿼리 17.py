import sys

input = sys.stdin.readline
INF = 1000000001


def build(node, left, right):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]

    mid = (left + right) // 2
    leftVal = build(node * 2, left, mid)
    rightVal = build(node * 2 + 1, mid + 1, right)

    segment_tree[node] = min(leftVal, rightVal)
    return segment_tree[node]


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        segment_tree[node] = value
        return segment_tree[node]

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    segment_tree[node] = min(segment_tree[node * 2], segment_tree[node * 2 + 1])


def find(node, start, end, left, right):
    if start > right or end < left:
        return INF

    if left <= start and end <= right:
        return segment_tree[node]

    mid = (start + end) // 2

    return min(find(node * 2, start, mid, left, right), find(node * 2 + 1, mid + 1, end, left, right))


if __name__ == '__main__':
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    segment_tree = [0] * n * 4
    build(1, 1, n)

    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 1, n, b, c)
        else:
            print(find(1, 1, n, b, c))
