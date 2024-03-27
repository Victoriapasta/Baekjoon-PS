import sys
input = sys.stdin.readline

while True:
    a, b, c = input().split()
    if a == '#' and b == c:
        exit(0)
    if int(b) > 17 or int(c) >=80:
        print(a + " Senior")
    else:
        print(a + " Junior")