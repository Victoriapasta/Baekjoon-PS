import sys

input = sys.stdin.readline

n = int(input())

matrix_a = [[1, 1], [1, 0]]


def matrix_product(a, b):
    result_matrix = [[0] * len(b[0]) for _ in range(2)]

    for row in range(2):
        for column in range(2):
            for i in range(2):
                result_matrix[row][column] += a[row][i] * b[i][column] % 1000000007

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


answer_matrix = divide_and_conquer(matrix_a, n)

print(answer_matrix[0][1] % 1000000007)