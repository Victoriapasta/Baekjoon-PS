import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

segmentTree = [0 for _ in range(n * 4)]


def build(target, leftNode, rightNode):
    if leftNode == rightNode:
        segmentTree[target] = arr[leftNode]
        return segmentTree[target]

    parentNode = (leftNode + rightNode) // 2
    leftValue = build(target * 2, leftNode, parentNode)
    rightValue = build(target * 2 + 1, parentNode + 1, rightNode)
    segmentTree[target] = leftValue + rightValue
    return segmentTree[target]


def find(start, end, target, leftNode, rightNode):
    if rightNode < start or end < leftNode:
        return 0
    if start <= leftNode and rightNode <= end:
        return segmentTree[target]

    parentNode = (leftNode + rightNode) // 2
    leftValue = find(start, end, target * 2, leftNode, parentNode)
    rightValue = find(start, end, target * 2 + 1, parentNode + 1, rightNode)
    return leftValue + rightValue


def update(target, leftNode, rightNode, index, value):
    if leftNode == rightNode == index:
        segmentTree[target] = value
        return
    if index < leftNode or rightNode < index:
        return

    parentNode = (leftNode + rightNode) // 2
    update(target * 2, leftNode, parentNode, index, value)
    update(target * 2 + 1, parentNode + 1, rightNode, index, value)
    segmentTree[target] = segmentTree[target * 2] + segmentTree[target * 2 + 1]


build(1, 0, n - 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    else:
        answer = find(b - 1, c - 1, 1, 0, n - 1)
        print(answer)
