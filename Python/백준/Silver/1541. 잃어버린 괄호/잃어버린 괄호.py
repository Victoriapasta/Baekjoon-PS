import sys
input = sys.stdin.readline

expression = list(input().strip().split('-'))

answer = sum(map(int, expression[0].split('+')))

for char in expression[1:]:
    temp = sum(map(int, char.split('+')))
    answer -= temp

print(answer)