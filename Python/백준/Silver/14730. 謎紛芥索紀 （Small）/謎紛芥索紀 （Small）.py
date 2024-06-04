def diff(ex):
    return ex[0] * ex[1]


if __name__ == '__main__':
    n = int(input())
    expression = []
    answer= 0

    for _ in range(n):
        expression.append(list(map(int, input().split())))

    for ex in expression:
        answer += diff(ex)

    print(answer)