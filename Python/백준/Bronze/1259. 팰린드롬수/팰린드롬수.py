import sys

input = sys.stdin.readline

while True:
    number = str(input().rstrip())

    if number == '0':
        break

    isPalindrome = True
    for i in range(len(number) // 2):
        if number[i] != number[-i - 1]:
            isPalindrome = False

    if isPalindrome:
        print('yes')
    else:
        print('no')
