x, y = map(str, input().split())
print(int(''.join(reversed(str(int(''.join(reversed(x))) + int(''.join(reversed(y))))))))