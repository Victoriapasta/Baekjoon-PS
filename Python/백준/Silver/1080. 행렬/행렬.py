import sys

input = sys.stdin.readline

n, m = map(int, input().split())

input_matrix = []
output_matrix = []
count = 0

for _ in range(n):
    input_matrix.append(list(map(str, input().rstrip())))

for _ in range(n):
    output_matrix.append(list(map(str, input().rstrip())))


def change(i, j):
    for _ in range(i, i + 3):
        for __ in range(j, j + 3):
            if input_matrix[_][__] == '0':
                input_matrix[_][__] = '1'
            else:
                input_matrix[_][__] = '0'


if n < 3 or m < 3:
    if input_matrix != output_matrix:
        print(-1)
        exit(0)

for r in range(n - 2):
    for c in range(m - 2):
        if input_matrix[r][c] != output_matrix[r][c]:
            count += 1
            change(r, c)

if input_matrix != output_matrix:
    print(-1)
    exit(0)


print(count)
