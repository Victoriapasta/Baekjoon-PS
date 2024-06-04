def diff(poly):

    if poly[0] == 'x':
        return 1
    if len(poly) == 1:
        return 0
    if len(poly) <= 2:
        if poly[0] == '-' and poly[1] == 'x':
            return -1
        if poly[1] != 'x':
            return 0
    index = -1
    for i in range(len(poly)):
        if poly[i] == 'x':
            index = i

    if index == -1:
        return 0

    if index == 1:
        if poly[0] == '-':
            return -1

    return int(poly[:index])


if __name__ == '__main__':
    poly = str(input().rstrip())
    print(diff(poly))