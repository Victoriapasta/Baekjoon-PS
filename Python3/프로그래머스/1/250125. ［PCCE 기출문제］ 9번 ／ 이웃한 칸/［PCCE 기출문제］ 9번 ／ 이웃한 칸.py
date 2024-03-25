def solution(board, x, y):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == board[x][y]:
            answer += 1
    return answer