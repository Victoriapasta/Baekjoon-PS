def solution(n):
    answer = 1
    tmp = 0
    for i in range(1, n):
        for j in range(i, n):
            tmp += j
            if tmp == n:
                answer += 1
                tmp = 0
                break
            elif tmp > n:
                tmp = 0
                break
    return answer