## Лабораторная_01</h1>
### Номер 01
```python
n = str(input("Имя: "))
v = int(input("Возраст: "))
v += 1
print("Привет, ", n, "! Через год тебе будет ", v, ".", sep = '')
```
<img width="1522" height="784" alt="ex01" src="https://github.com/user-attachments/assets/053191f9-4998-48b9-8638-8f2c7d58ff49" />
Принимаю на ввод имя и возраст, вывожу тоже самое, добавляя к возрасту один год.

### Номер 02
```python
a = str(input("a: "))
a = a.replace(',', '.')
a = float(a)
b = str(input("b: "))
b = b.replace(',', '.')
b = float(b)
s = round(a + b, 2)
avg = round(s / 2, 2)
print('sum=', s, '; avg=', avg, sep='')
```
<img width="1254" height="1230" alt="ex02" src="https://github.com/user-attachments/assets/6a794dfd-a932-4e02-86ce-bbe9531f2e1e" />
Принимаю два числа со знаками после точки, однако на вход могут подаваться числа с запятой, вместо точки. Такую возможность я реализовал путем того, что принимал числа в формате str, а затем заменял в них запятую на точку, если таковая была. После числа переводились в формат float и с ними проводились требуемые операции. Учел необходимость размещать только два знака после запятой при помощи функции round.

### Номер 03 
```python
p = int(input("Введите цену:"))
d = int(input("Введите скидку:"))
v = int(input("Введите налог: "))
b = round(p * (1 - d/100), 2)
vr = round(b * (v/100), 2)
t = round(b + vr, 2)
print(f"База после скидки: {b}₽")
print(f"НДС:               {vr}₽")
print(f"Итого к оплате:    {t}₽")
```
<img width="1498" height="1178" alt="ex03" src="https://github.com/user-attachments/assets/c57cb99e-2df2-43e5-9c20-0f9bf4c70987" />
Ничего примечательного, реализовал вывод чисел через f строки.

### Номер 04
```python
m = int(input("Минуты: "))
h = m // 60
om = m - h * 60
if om < 10:
    om = str('0' + str(om))
print(h, ':', om, sep = '')
```
<img width="966" height="1160" alt="ex04" src="https://github.com/user-attachments/assets/77505a11-b8f5-4bfa-a974-987c65966e48" />
Главная сложность задания - не упустить необходимость добавлять 0 перед записью минут, если их значнение меньше 10.

### Номер 05
```python
n = str(input("ФИО: "))
n = n.strip()
ns = n.split()
n1 = ns[0][0]
n2 = ns[1][0]
n3 = ns[2][0]
print(n1, n2, n3, '.', sep='')
print('Длинна (символов): ', len(ns[0]) + len(ns[1]) + len(ns[2]) + 2)
```
<img width="1498" height="1232" alt="ex05" src="https://github.com/user-attachments/assets/40e8794b-50d7-4f3c-b199-d78332586300" />
Принимаю строку с неизвестным количесвом пробелов, делаю из нее список, попутно удаляя все пробелы при помощи функций strip и split. ФИО составяю из первой буквы каждого слова, кол-во символов складываю из длинн слов + 2 два пробела между ними.

### Номер 06
```python
n = int(input('in_1: '))
finT = 0
finF = 0
for i in range(n):
    print('in_', i+2, ': ', end='', sep = '')
    p = str(input())
    s = p.split()
    if str(s[3]) == 'True':
        finT += 1
    else:
        finF += 1
print('out:', finT, finF)
```
<img width="1482" height="1222" alt="ex06" src="https://github.com/user-attachments/assets/5dd6f944-7e03-41dc-ae77-2f67e87adde3" />
Сначала принимаю кол-во будущих строк, затем при помощи цикла for превращаю каждую из них в спискок (функция split), и проверяю что стоит под индексом 3 в каждом из них, провожу подсчет и вывожу результат.

### Номер 07
```python
s = str(input('in: '))
w = []
for i in range(len(s)):
    w.append(s[i])
for i in range(len(w)):
    if w[i].isupper():
        n1 = i
        break
for i in range(len(w)):
    if w[i].isdigit():
        n2 = i + 1
        break
r = n2 - n1
k = (len(s) - n2) // r
fin = w[n1] + w[n2]
for i in range(1, k + 1):
    fin = fin + w[n2 + r * i]
print('out:', fin)
```
<img width="1504" height="1226" alt="ex07" src="https://github.com/user-attachments/assets/409e55e1-822b-4c8d-87ed-aa213abede17" />
Принимаю на вход зашифрованное сообщение, зная, что шаг между символами настоящего сообшения фиксированный, нахожу индекс первой буквы (зная что она находится в верхнем регистре) при помщи перебора и функции isupper. Второй символ находится сразу после цифры, поэтому находим ее индекс при помощи перебора и функции isdigit, а затем добавляем 1 к результату. После этого нахожу разницу между индексами, чтобы понять шаг, по которому находятся нужные символы. Расчитываю сколько всего символов в истинном сообщении и при помощи цикла for, зная их индексы добавляю их к предыдущим двум буквам, получая расшифрованное сообщение.

## Лабораторная_02</h1>
### Номер 01
```python
def min_max(a):
    if len(a) > 0:
        return (min(a), max(a))
    else:
        return 'ValueError'
def unique_sorted(b):
    b = set(b)
    b = sorted(list(b))
    return b
def flatten(c):
    d = []
    for i in range(len(c)):
        if (type(c[i]) == list) or (type(c[i]) == tuple):
            d.extend(c[i])
        else:
            return 'TypeError'
    return d
print('min_max:')
print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5, -2, -9]), sep = '\n')
print(min_max([]), min_max([1.5, 2, 2.0, -3.1]), ' ', sep = '\n')
print('unique_sorted:')
print(unique_sorted([3, 1, 2, 1, 3]), unique_sorted([]), sep = '\n')
print(unique_sorted([-1, -1, 0, 2, 2]), unique_sorted([1.0, 1, 2.5, 2.5, 0]), ' ', sep = '\n')
print('flatten:')
print(flatten([[1, 2], [3, 4]]), flatten(([1, 2], (3, 4, 5))), flatten([[1], [], [2, 3]]), sep = '\n')
print(flatten([[1, 2], "ab"]))
```
<img width="1710" height="1266" alt="ex_01" src="https://github.com/user-attachments/assets/e834b96d-4be5-4c67-b93b-2d51790799c3" />
Функция min_max реализуется при помощи встроенных функций питона min и max. Для функции unique_sorted я сначала превратил список в множество, чтобы оставить только уникальные значения, затем при помощи функции sorted сортирую их. Для функции flatten я использовал простой перебор и добавление элементов внутренних списков в один общий. Так же для каждой функции я добавил проверку на соответствие поступаемых данных.

### Номер 02
```python
def transpose(a):
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

def row_sums(a):
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ans = []
    for i in range(len(a)):
        ans.append(sum(a[i]))
    return ans

def col_sums(a):
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
print('transpose:')
print(transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3, 4]]), sep = '\n')
print(transpose([]), transpose([[1, 2], [3]]), sep = '\n')

print(' ', 'row_sums:', sep = '\n')
print(row_sums([[1, 2, 3], [4, 5, 6]]), row_sums([[-1, 1], [10, -10]]), sep = '\n')
print(row_sums([[0, 0], [0, 0]]), row_sums([[1, 2], [3]]), sep = '\n')

print(' ', 'col_sums:', sep = '\n')
print(col_sums([[1, 2, 3], [4, 5, 6]]), col_sums([[-1, 1], [10, -10]]), sep = '\n')
print(col_sums([[0, 0], [0, 0]]), col_sums([[1, 2], [3]]), sep = '\n')
```
<img width="1720" height="1278" alt="ex_02" src="https://github.com/user-attachments/assets/ecbb9ff3-4b2e-4a37-b5fd-621880a855a1" />
Для функции transpose, я ввел проверку на рваные матрицы, которую затем копировал во все остальне функции. Затем создал список и при помощи перебора по особому алгоритму добавлял туда значения. Функция row_sums работает при помощи sum, я просто суммирую содержимое каждого списка внутри матрицы. col_sums работает таким образом, что просто перебирает индексы столбцов, суммирует их содержимое и добавляет в список для ответа.

### Номер 03
```python
def tuples(a):
    if type(a[0]) != str or type(a[1]) != str or type(a[2]) != float or type(a) != tuple:
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
```
<img width="1716" height="1280" alt="ex_03" src="https://github.com/user-attachments/assets/12a3f83e-3b1b-446f-b1a2-466b7c087972" />
Для начала я проверию на соответсвие типов данных, затем на величину показателя GPA, он не должен превышать 5.0. Еще одна проверка необходима, чтобы знать, что в ФИО не попадет только одно слово. Затем при помощи перебора и функции capitalize(делает первую букву строки большой), я составляю ФИО и делаю вывод со всеми необходимыми переменными. Далее я добавил несколько дополнительных тест-кейсов, чтобы показать работу моих проверок.

## Лабораторная_03</h1>
### задание A
```python
def normalize(text, casefold, yo2e):
    if casefold != False:
        text = text.casefold()
    if yo2e != False:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\b', ' ')
    spis = text.split()
    text = ''
    for i in range(len(spis)):
        text += spis[i]
        text += ' '
    text = text.strip()
    return text
def tokenize(text):
    raz = ['!', ',', '😀', '—', ':', ';', '?', '/', '&', '*', '#', '$', '%', '.']
    for i in range(len(text)):
        if text[i] in raz:
            text = text.replace(text[i], ' ')
    spis = text.split()
    return spis
def count_freq(t):
    fin = {}
    uni = set(t)
    uni = list(uni)
    uni = sorted(uni)
    kol = []
    for i in range(len(uni)):
        kol.append(t.count(uni[i]))
    kol_u = set(kol)
    kol_u = sorted(list(kol_u), reverse=True)
    for i in kol_u:
        for j in uni:
            if t.count(j) == i:
                fin.update({j:i})
    return fin
def top_n(t, n):
    fin = []
    uni = set(t)
    uni = list(uni)
    uni = sorted(uni)
    kol = []
    for i in range(len(uni)):
        kol.append(t.count(uni[i]))
    kol_u = set(kol)
    kol_u = sorted(list(kol_u), reverse=True)
    for i in kol_u:
        for j in uni:
            if t.count(j) == i:
                fin.append((j, i))
    fin_s = []
    if n > len(uni):
        n = len(uni)
    for i in range(n):
        fin_s.append(fin[i])
    return fin_s
'''
print('normalize:')
print(normalize("ПрИвЕт\nМИр\t", True, True), normalize('ёжик, Ёлка', True, True), sep = '\n')
print(normalize("Hello\r\nWorld", True, True), normalize("  двойные   пробелы  ", True, True), sep='\n')
print('', 'tokenize:', sep = '\n')
print(tokenize("привет мир"), tokenize("hello,world!!!"), sep = '\n')
print(tokenize("по-настоящему круто"), tokenize("2025 год"), sep = '\n')
print(tokenize("emoji 😀 не слово"))
print(' ', 'count_freq + top_n:', sep = '\n')
print('Частоты:', count_freq(["a","b","a","c","b","a"]), 'Топ:', top_n(["a","b","a","c","b","a"], 2))
print('Частоты:', count_freq(["bb","aa","bb","aa","cc"]), 'Топ:', top_n(["bb","aa","bb","aa","cc"], 2))
'''
```
![text](https://github.com/user-attachments/assets/d59ba110-70f5-416f-93a8-a5af2e75a446)
normalize: 
Для начала реализую работу casefold и yo2e при помощи .replace и .casefold, затем, в цикле перебираю текст, чтобы собрать его в готовом виде.
tokenize:
Создаю список со всеми разделителями, при помощи цикла и функции replace заменяю их в тексте на пробелы. Превращаю текст в список функцией split.

count_freq:
Сначала, через множество и sorted создаю список уникальных слов из текста по алфавиту, затем нахожу их частоту в тексте так, чтобы у слова и его частоты в списке был одинаковый индекс. Уже знакомым способом создаю список уникальных значений частот, а затем перебирая уникальные значения в порядке убывания, добавляю в словарь пары слово:частота.

top_n:
Делаю все аналогично функции count_freq, за исключением того, что в конце вместо словаря используется список и кортежи вида (слово, частота). После получения списка с кортежами, я создаю его финальный вариант, куда добавляю топ-5 значений по величине, если уникальных слов меньше, n принимает значение их количества.

### задание B
```python
from ..lib.text import normalize, tokenize, top_n
text = input()
text = normalize(text, True, True)
text = tokenize(text)
print('Всего слов:', len(text))
print('Уникальных слов:', len(set(text)))
sp = top_n(text, 5)
sl = []
for i in range(len(sp)):
    sl.append(len(sp[i][0]))
m = max(sl)
print('табличный режим(on/off):')
vkl = input()
print('Топ-5:')
if m < len('Слово'):
    m = len('Слово')
if vkl == 'on':
    print('Слово', ' ' * (m - len('Слово')), '|', ' частота', sep = '')
    print('-' * m, '-' * 9, sep = '')
    for i in range(len(sp)):
        print(sp[i][0], ' ' * (m - len(sp[i][0])), '| ', sp[i][1], sep = '')
else:
    for i in range(len(sp)):
        print(sp[i][0], ':', sp[i][1], sep = '')

```

![text_stats](https://github.com/user-attachments/assets/fe689c82-02e7-462d-b0e8-f0bde2bf3010)
![text_stats_on_off](https://github.com/user-attachments/assets/8038aff2-fb17-41d7-a8fc-898042e25a6a)

В начале, при помощи относительного импорта добавляю функции normalize, tokenize, top_n. Затем провожу вводимый пользователем текст через функции normalize и tokenize, чтобы получить список слов. Далее нахожу сколько всего слов при помощи длинны этого списка, и сколько из них уникальных, создавая из списка множество. Далее стоит переключатель, он решает в каком виде будет производиться вывод. В случае обычного вывода, текст проходит через top_n и выводит значения по порядку, но в случае табличного, сначала необходимо найти длинну самого длинного слова в топе, под него подстраивается вся таблица, только не в случае если оно короче заголовка. Таблица выводится при помощи умножения символов по формуле ((длинна самого большого слова) - (длинна выводимого слова)) * (" "), а разделяющая полоска просто умножением "-" на длинну макс. слова + длинну остальной строки. Далее вставляю примеры текстов и выводов программы:
```
1) Сшит колпак да не по-колпаковски, вылит колокол да не по-колоколовски. Надо колпак переколпаковать, перевыколпаковать, надо колокол переколоколовать, перевыколоколовать
Всего слов: 18
Уникальных слов: 13
табличный режим(on/off):
on
Топ-5:
Слово  | частота
----------------
да     | 2
колокол| 2
колпак | 2
надо   | 2
не     | 2
2)На дворе дрова, за двором дрова, дрова вширь двора, не вместит двор дров, надо дрова выдворить на дровяной двор.
Всего слов: 19
Уникальных слов: 15
табличный режим(on/off):
off
Топ-5:
дрова:4
на:2
вместит:1
вширь:1
выдворить:1
3)Может бахнем? Обязательно бахнем, только не сейчас.
Всего слов: 7
Уникальных слов: 6
табличный режим(on/off):
on
Топ-5:
Слово      | частота
--------------------
бахнем     | 2
может      | 1
не         | 1
обязательно| 1
сейчас     | 1
```

## Лабораторная_04</h1>
### Задание А
```python
from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str: # FileNotFoundError и UnicodeDecodeError могут появляться
    p = Path(path)
    t = str(p.read_text(encoding=encoding))
    t = t.strip()
    s = t.split() #преобразуем текст в список слов
    fin = ''
    for i in range(len(s)): #делаем из нескольких строк одну
        fin = fin + s[i] + ' '
    return fin.strip()

file_name = input('Введите название файла в папке data (по умолчанию - input.txt): ') #по желанию пользователя может быть выбран другой файл
if file_name == '':
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt" #по умолчанию используется файл input.txt
else:
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04" + f'\{file_name}'
cod = input('Введите кодировку файла (по умолчанию - utf-8): ') #по желанию пользователя, может быть выбрана другая кодировка
if cod == '':
    cod = 'utf-8' #по умолчанию кодировка utf-8
print(read_text(file_path, cod)) #пользователь может выбрать другую кодировку или расположения файла, если изменит их при запуске программы


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    d = len(rows[0]) #замер на длинну одной из строк
    for i in rows: #проверка на одинаковую длинну строк
        if len(i) != d:
            raise ValueError #вывод ValueError если длинна не совпадает
    p.parent.mkdir(parents=True, exist_ok=True) #создание родительской директории
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

write_csv([("Проект А", "100000", "80000", "20000"), ("Проект Б", "50000", "45000", "5000"), ("Проект В", "75000", "60000", "15000")], Path("C:/Users/kuzne/Desktop/laby_piton/python_labs/src/data/lab04/report.csv"), ("Проект", "Доход", "Расход", "Прибыль"))
```

соджержимое input.txt:
```
Шла саша по шоссе
И сосала сушку

```
![io_txt_csv_code](https://github.com/user-attachments/assets/5be6db3c-9757-407a-a7a9-7bf4817769c0)

В функции read_text я добавил возможность переводить многострочный текст в одну строку, так же написал небольшой скрипт, благодаря которому пользователь может сам выбрать название файла для считывания в папке и его кодировку.

В функции write_csv я добавил проверку на одинаковую длинну строк, в случае провала которой выводится ValueError. Затем я добавил создание родительских директорий при помощи методов .parent и .mkdir. Далее будет скриншот того, как выглядел csv файл после работы функции:

![io_txt_csv_report](https://github.com/user-attachments/assets/8bd74b7f-c443-45e5-8a18-36190b1b945a)

Вывод ошибки в случае "рваных" строк:

![io_error](https://github.com/user-attachments/assets/fd0c97cd-461d-4574-be7c-c6e061be643c)

так же к заданию прилагался тест:
```python
from io_txt_csv import read_text, write_csv
txt = read_text(r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
```
Содержимое файла после работы теста:

![io_check](https://github.com/user-attachments/assets/2967fae0-84f1-4ba5-aa2d-9a94b73aadf5)

### Задание B
