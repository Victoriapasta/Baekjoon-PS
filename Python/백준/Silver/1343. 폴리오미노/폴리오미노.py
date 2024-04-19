import sys

input = sys.stdin.readline
board = str(input())
newboard = ''

if board.rstrip() == 'X':
    print(-1)
    exit(0)

temp = 0
for i in range(len(board)):
    if temp == 2:
        newboard += 'BB'
        temp = 0
    if board[i] == 'X':
        temp += 1
    if board[i] == '.':
        newboard += '.'
        if temp:
            print(-1)
            exit(0)

answer = newboard.replace('BBBB', 'AAAA')
if len(answer) == len(board.rstrip()):
    print(answer)
else:
    print(-1)
