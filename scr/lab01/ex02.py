a = str(input("a: "))
a = a.replace(',', '.')
a = float(a)
b = str(input("b: "))
b = b.replace(',', '.')
b = float(b)
s = a + b
avg = s / 2
print('sum = ', s, '; avg= ', avg, sep='')
