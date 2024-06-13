import sys

input = sys.stdin.readline
INF = 1000000001


def build(node, leftNode, rightNode):
    if leftNode == rightNode:
        segmentTree[node] = arr[leftNode]
        return segmentTree[node]

    mid = (leftNode + rightNode) // 2

    segmentTree[node] = min(build(node * 2, leftNode, mid), build(node * 2 + 1, mid + 1, rightNode))
    return segmentTree[node]


def find(node, start, end, left, right):
    if start > right or end < left:
        return INF

    if left <= start and end <= right:
        return segmentTree[node]

    mid = (start + end) // 2

    return min(find(node * 2, start, mid, left, right), find(node * 2 + 1, mid + 1, end, left, right))


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    segmentTree = [0] * n * 4
    build(1, 0, n - 1)

    for _ in range(m):
        a, b = map(int, input().split())
        print(find(1, 0, n - 1, a - 1, b - 1))
