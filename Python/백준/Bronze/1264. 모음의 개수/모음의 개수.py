while True:
    s = str(input())
    answer = 0
    if s == '#':
        break
    dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for i in s:
        if i in dic:
            dic[i] += 1

    for i in dic:
        answer += dic[i]

    print(answer)
