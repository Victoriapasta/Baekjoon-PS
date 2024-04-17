a, b = map(str, input().split())

temp1, temp2, temp3 = a[2], a[1], a[0]
temp4, temp5, temp6 = b[2], b[1], b[0]

a = int(temp1 + temp2 + temp3)
b = int(temp4 + temp5 + temp6)

print(max(a, b))
