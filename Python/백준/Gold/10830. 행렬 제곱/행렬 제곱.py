import sys

input = sys.stdin.readline

An, B = map(int, input().split())

matrix_a = []

for i in range(An):
    matrix_a.append(list(map(int, input().split())))


def matrix_product(a, b):
    result_matrix = [[0] * An for _ in range(An)]

    for row in range(len(a)):
        for column in range(len(b[0])):
            for i in range(len(a[row])):
                result_matrix[row][column] += a[row][i] * b[i][column] % 1000

    return result_matrix


def divide_and_conquer(a, b):
    if b == 1:
        return a
    else:
        temp = divide_and_conquer(a, b // 2)
        if not b % 2:
            return matrix_product(temp, temp)
        else:
            return matrix_product((matrix_product(temp, temp)), a)


answer_matrix = divide_and_conquer(matrix_a, B)

for col in answer_matrix:
    for row in range(len(col)):
        print(col[row] % 1000, end=' ')
    print()
