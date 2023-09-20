def solution(n):
    arr = sorted(list(str(n)), reverse = True)
    answer = ''
    for i in arr:
        answer += i
    return int(answer)