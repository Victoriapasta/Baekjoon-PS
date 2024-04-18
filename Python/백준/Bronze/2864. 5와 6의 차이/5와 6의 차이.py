a, b = map(str, input().split())

minA = a.replace('6', '5')
maxA = a.replace('5', '6')
minB = b.replace('6', '5')
maxB = b.replace('5', '6')

print(int(minA) + int(minB), int(maxA) + int(maxB))
