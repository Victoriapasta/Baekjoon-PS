x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
    exit(0)
if x < 0 and y < 0:
    print(3)
    exit(0)
if x > 0 and y < 0:
    print(4)
    exit(0)
if x < 0 and y > 0:
    print(2)
    exit(0)