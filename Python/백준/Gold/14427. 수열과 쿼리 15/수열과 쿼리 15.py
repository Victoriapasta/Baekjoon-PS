import sys

input = sys.stdin.readline


def Query(left, right):
    if arr[left] <= arr[right]:
        return left
    return right


def build(node, leftNode, rightNode):
    if leftNode == rightNode:
        segmentTree[node] = leftNode
        return segmentTree[node]

    mid = (leftNode + rightNode) // 2
    leftValue = build(node * 2, leftNode, mid)
    rightValue = build(node * 2 + 1, mid + 1, rightNode)

    segmentTree[node] = Query(leftValue, rightValue)
    return segmentTree[node]


def update(index, value, node, leftNode, rightNode):
    if index < leftNode or index > rightNode:
        return segmentTree[node]

    if leftNode == rightNode:
        arr[index] = value
        return segmentTree[node]

    mid = (leftNode + rightNode) // 2
    leftValue = update(index, value, node * 2, leftNode, mid)
    rightValue = update(index, value, node * 2 + 1, mid + 1, rightNode)

    segmentTree[node] = Query(leftValue, rightValue)
    return segmentTree[node]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    segmentTree = [0] * (n * 4)
    build(1, 0, n - 1)

    m = int(input())
    for _ in range(m):
        a, *b = map(int, input().split())
        if a == 1:
            update(b[0] - 1, b[1], 1, 0, n - 1)
        else:
            print(segmentTree[1] + 1)
