import sys

input = sys.stdin.readline


def find(node, start, end, left, right):
    if right < start or left > end:
        return 0

    if left <= start and end <= right:
        return segment_tree[node]

    mid = (start + end) // 2
    leftVal = find(node * 2, start, mid, left, right)
    rightVal = find(node * 2 + 1, mid + 1, end, left, right)

    return leftVal + rightVal


def update(node, start, end, left, right):
    if left < start or left > end:
        return

    if start == end:
        segment_tree[node] = right
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right)
    update(node * 2 + 1, mid + 1, end, left, right)

    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]


if __name__ == '__main__':
    n, m = map(int, input().split())

    segment_tree = [0] * n * 4

    for _ in range(m):
        a, b, c = map(int, input().split())

        if a == 0:
            if b > c:
                b, c = c, b
            print(find(1, 0, n - 1, b - 1, c - 1))
        else:
            update(1, 0, n - 1, b - 1, c)
