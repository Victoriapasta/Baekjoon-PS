import sys

input = sys.stdin.readline


def solution(n, read):
    stack = []
    answer = 0
    read.append(0)

    for i in range(n + 1):
        val = read[i]
        start = i
        while stack and stack[-1][1] >= val:
            start, hei = stack.pop()
            answer = max(answer, (i - start) * hei)
        stack.append([start, val])

    return answer


if __name__ == '__main__':
    while True:
        read = list(map(int, input().split()))
        n = read[0]
        if n == 0:
            break
        print(solution(n, read[1:]))
