def solution(numbers):
    answer = {}
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            answer[numbers[i]+j] = 1
    return sorted(list(answer.keys()))