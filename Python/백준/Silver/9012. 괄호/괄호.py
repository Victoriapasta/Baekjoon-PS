import sys
input = sys.stdin.readline

def Matching(formula):
    stack = []

    for i in range(len(formula)):
        if formula[i] == '(':
            stack.append(formula[i])
        elif formula[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

T = int(input())

for i in range(T):
    formula = str(input())
    if Matching(formula) == True:
        print('YES')
    else:
        print('NO')