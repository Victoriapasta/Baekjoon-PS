t = int(input())

for testcase in range(t):
    H, W, N = map(int, input().split())

    answer = 100

    answer *= N % H
    answer += N // H + 1

    if not N % H:
        answer = 100 * H + N // H

    print(answer)