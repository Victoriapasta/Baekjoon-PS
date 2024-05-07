while True:
    n = int(input())
    if n == -1:
        break

    temp = []

    for i in range(1, n):
        if not n % i:
            temp.append(i)

    if sum(temp) == n:
        print(n, ' = ', ' + '.join(str(i) for i in temp), sep='')

    else:
        print(n, 'is NOT perfect.')
