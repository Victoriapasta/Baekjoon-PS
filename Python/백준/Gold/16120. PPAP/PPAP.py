import sys

input = sys.stdin.readline


def isPPAP(string):
    stack = []
    for char in string:
        stack.append(char)
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(4):
                stack.pop()
            stack.append('P')

    if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
        return 'PPAP'
    else:
        return 'NP'


if __name__ == '__main__':
    s = str(input().rstrip())
    print(isPPAP(s))
