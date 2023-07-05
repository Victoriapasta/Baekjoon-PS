import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 1
tmp = 1

for i in range(k):
    cnt *= (n-i)
    tmp *= (i+1)

ans = cnt//tmp
print(ans % 10007)