import sys

input = sys.stdin.readline

sentence = list(input())

stack = []
postfix = []
priority = {"*": 2, "/": 2, "+": 1, "-": 1, '(': 0}

for word in sentence[:-1]:
    if word in priority:
        while stack and priority[stack[-1]] >= priority[word] and word != '(':
            postfix.append(stack.pop())
        stack.append(word)
    else:
        if word == '(':
            stack.append(word)
        if word == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(word)

while stack:
    postfix.append(stack.pop())

print("".join(postfix))
