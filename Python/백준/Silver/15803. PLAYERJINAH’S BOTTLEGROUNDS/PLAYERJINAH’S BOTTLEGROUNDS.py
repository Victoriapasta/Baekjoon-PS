x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def ccw():
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

if ccw():
    print('WINNER WINNER CHICKEN DINNER!')
else:
    print('WHERE IS MY CHICKEN?')
