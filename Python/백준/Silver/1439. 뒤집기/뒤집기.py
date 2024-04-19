import sys
input = sys.stdin.readline

s = str(input())

zeros = 0
ones = 0
temp = ''
for number in s:
    if len(temp) >= 1 and temp[-1] != number:
        if temp[-1] == '0':
            zeros += 1
        else:
            ones += 1

    if number == '0':
        temp += '0'
    if number == '1':
        temp += '1'

print(min(zeros, ones))