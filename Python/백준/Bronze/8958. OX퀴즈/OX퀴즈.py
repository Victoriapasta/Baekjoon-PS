import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    score = 0
    temp = 1
    answer = str(input().rstrip())
    for char in answer:
        if char == 'O':
            score += temp
            temp += 1
        else:
            temp = 1
    print(score)