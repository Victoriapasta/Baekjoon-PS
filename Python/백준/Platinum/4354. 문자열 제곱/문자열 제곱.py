import sys
from math import sqrt

input = sys.stdin.readline


def kmp(l):
    answer = []
    for i in range(1, int(sqrt(l)) + 1):
        if not l % i:
            answer.append(i)
            if i != l // i:
                answer.append(l // i)

    return sorted(answer, reverse=True)


if __name__ == '__main__':
    for _ in range(10):
        s = str(input().rstrip())
        if s == '.':
            break

        sLen = len(s)
        sCase = kmp(sLen)

        temp = 0
        for i in sCase:
            if s == s[:sLen // i] * i:
                temp = i
                break
        print(temp)