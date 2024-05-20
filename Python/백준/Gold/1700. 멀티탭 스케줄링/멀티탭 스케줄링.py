import sys
input = sys.stdin.readline

INF = int(10 ** 9)
n, k = map(int, input().split())

tap = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(k):
    if tap[i] in plug:
        continue

    if len(plug) < n:
        plug.append(tap[i])
        continue

    p = []

    for j in plug:
        if j in tap[i:]:
            p.append(tap[i:].index(j))
        else:
            p.append(INF)

    use = p.index(max(p))
    plug.remove(plug[use])
    plug.append(tap[i])
    cnt += 1

print(cnt)