import sys

input = sys.stdin.readline

min, max = map(int, input().split())

answer = max - min + 1
prime = [False for _ in range(answer)]

for i in range(2, int(max ** 0.5 + 1)):
    sqr = i ** 2
    for j in range((((min-1)//sqr)+1)*sqr, max+1, sqr):
        if not prime[j - min]:
            prime[j - min] = True
            answer -= 1

print(answer)