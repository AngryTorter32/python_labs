def tuples(a):
    if type(a[0]) != str or type(a[1]) != str or type(a[2]) != float:
        return 'TypeError'
    if a[2] > 5.00:
        return "ValueError"
    name = a[0].split()
    if len(name) < 2:
        return 'ValueError'
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    fio = str(name[0]) + ' '
    for i in range(1, len(name)):
        fio += name[i][0]
        fio += '. '
    fio = fio[:-1]
    return fio + ', ' + str(a[1])+ ', GPA ' + str(round(a[2], 2))
print(tuples(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(tuples(("Петров Пётр", "IKBO-12", 5.0)))
print(tuples(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(tuples(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
