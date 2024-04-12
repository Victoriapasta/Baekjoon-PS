n = int(input())

for num in range(1, n+1):
    temp = sum(map(int, str(num)))
    summary = temp + num
    if summary == n:
        print(num)
        break
    if num == n:
        print(0)
        break