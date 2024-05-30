x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def ccw(x1, y1, x2, y2, x3, y3):
   return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


answer = ccw(x1, y1, x2, y2, x3, y3)

if answer > 0:
    print(1)
    exit(0)
if answer == 0:
    print(0)
    exit(0)
if answer < 0:
    print(-1)
    exit(0)