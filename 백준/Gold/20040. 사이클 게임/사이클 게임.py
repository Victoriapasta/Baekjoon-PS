import sys
input = sys.stdin.readline

class unionFind:
    graph = []
    great = []
    found = 0
    def find(self, node:int) -> int:
        if self.graph[node] < 0:
            return node
        else:
            return self.find(self.graph[node])

    def merge(self, a:int, b:int, c:int):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            self.found = c
            self.great.append(c)
            return
        if self.graph[a] <= self.graph[b]:
            self.graph[a] += self.graph[b]
            self.graph[b] = a
        else:
            self.graph[b] += self.graph[a]
            self.graph[a] = b

if __name__ == "__main__":
    ds = unionFind()
    cnt = 0

    n, m = map(int, input().split())
    ds.graph = [-1 for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        ds.merge(a, b, i+1)

    if ds.great:
        print(ds.great[0])
    else:
        print(0)