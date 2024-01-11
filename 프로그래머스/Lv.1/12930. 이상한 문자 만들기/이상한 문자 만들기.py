def solution(s):
    s = s.split(' ')
    answer = []
    for words in s:
        temp = ''
        for alphabet in range(len(words)):
            if alphabet % 2:
                temp += words[alphabet].lower()
            else:
                temp += words[alphabet].upper()
        answer.append(temp)
    return ' '.join(answer)