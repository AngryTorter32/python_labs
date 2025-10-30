n = str(input("ФИО: "))
n = n.strip()
ns = n.split()
n1 = ns[0][0]
n2 = ns[1][0]
n3 = ns[2][0]
print(n1, n2, n3, '.', sep='')
print('Длинна (символов): ', len(ns[0]) + len(ns[1]) + len(ns[2]) + 2)
