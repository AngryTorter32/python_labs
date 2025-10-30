m = int(input("Минуты: "))
h = m // 60
om = m - h * 60
if om < 10:
    om = str('0' + str(om))
print(h, ':', om, sep = '')
