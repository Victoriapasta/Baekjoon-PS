import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(n):
    name = str(input().rstrip())
    if name[0] in dic:
        dic[name[0]] += 1
    else:
        dic[name[0]] = 1

answer = ''
for i in dic.keys():
    if dic[i] >= 5:
        answer += i

answer = ''.join(sorted(answer))
if not answer:
    print('PREDAJA')
else:
    print(answer)
