import sys

input = sys.stdin.readline

An, Am = map(int, input().split())

matrix_a = []
matrix_b = []

for i in range(An):
    matrix_a.append(list(map(int, input().split())))

Bn, Bm = map(int, input().split())

for i in range(Bn):
    matrix_b.append(list(map(int, input().split())))


def matrix_product(a, b):
    result_matrix = [[0] * Bm for _ in range(An)]

    for row in range(len(a)):
        for column in range(len(b[0])):
            for i in range(len(a[row])):
                result_matrix[row][column] += a[row][i] * b[i][column]

    return result_matrix


answer_matrix = matrix_product(matrix_a, matrix_b)

for col in answer_matrix:
    for row in range(len(col)):
        print(col[row], end=' ')
    print()
