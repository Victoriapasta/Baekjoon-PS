def solution(s):
    answer = s[0].upper()
    for i in range(len(s)-1):
        if s[i] == ' ':
            answer += s[i+1].upper()
        else:
            answer += s[i+1].lower()
    return answer