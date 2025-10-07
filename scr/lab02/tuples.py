def tuples(a):
    if type(a[0]) != str or type(a[1]) != str or type(a[2]) != float:
        return 'TypeError' #проверяю на соответсвие типа данных и вывожу ошибку, если неверно
    if a[2] > 5.00:
        return "ValueError" #GPA не может быть больше 5.0
    name = a[0].split()
    if len(name) < 2:
        return 'ValueError' #Необходимо хотя бы два слова в ФИО
    for i in range(len(name)):
        name[i] = name[i].capitalize() #capitalize делает первую букву слова большой
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
print(tuples((2007, 'BIVT-25-2', 4.0))) #проверяю, определяет ли программа ошибку типа данных
print(tuples(('Илья Кузнецов', 'BIVT-25-2', 10.0))) #проверяю, видит ли программа ошибку значения данных
print(tuples(("Илья", 'BIVT-25', 5.0))) #проверяю, видит ли программа, что нужно хотя бы два слова в ФИО
print(tuples(('Кузнецов Илья Дмитриевич', 'BIVT-25-2', 5.0))) #проверка своего имени
