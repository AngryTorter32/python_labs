def min_max(a): #Вернуть кортеж (минимум, максимум). Если список пуст — ValueError.
    if len(a) > 0:
        return (min(a), max(a))
    else:
        return 'ValueError'

def unique_sorted(b): #Вернуть отсортированный список уникальных значений (по возрастанию).
    b = set(b)
    b = sorted(list(b))
    return b

def flatten(c): #«Расплющить» список списков/кортежей в один список по строкам
    d = []
    for i in range(len(c)):
        if (type(c[i]) == list) or (type(c[i]) == tuple):
            d.extend(c[i])
        else:
            return 'TypeError'
    return d

def transpose(a): #Поменять строки и столбцы местами.
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ansA = []
    y = len(a)
    x = len(a[0])
    for i in range(x):
        ansS = []
        for j in range(y):
            ansS.append(a[j][i])
        ansA.append(ansS)
    return ansA

def row_sums(a): #Сумма по каждой строке. 
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ans = []
    for i in range(len(a)):
        ans.append(sum(a[i]))
    return ans

def col_sums(a): #Сумма по каждому столбцу.
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ans = []
    for j in range(len(a[0])):
        c = 0
        for i in range(len(a)):
            c += a[i][j]
        ans.append(c)
    return ans
