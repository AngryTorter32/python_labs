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
```python
from ..lib.text import normalize, tokenize, top_n
from ..lib.io_txt_csv import read_text, write_csv

file_name = input('Введите название файла в папке data (по умолчанию - input.txt): ') #по желанию пользователя может быть выбран другой файл
if file_name == '':
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt" #по умолчанию используется файл input.txt
else:
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04" + f'\{file_name}'
cod = input('Введите кодировку файла (по умолчанию - utf-8): ') #по желанию пользователя, может быть выбрана другая кодировка
if cod == '':
    cod = 'utf-8' #по умолчанию кодировка utf-8
t = read_text(file_path, cod)
t = normalize(t, True, True) #нормализация
s = tokenize(t) #токенизация
uni = set(s) #уникальные слова
top = top_n(s, len(uni)) #нахожу частоты
top.insert(0, ('word', 'count')) #добавляю заголовок
write_csv(top, r'C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\report.csv') #запись отчета
print('Всего слов: ', len(s))
print('Уникальных слов: ', len(uni))
print('Топ-5:')
top5 = top_n(s, 5)
for i in range(len(top5)):
        print(top5[i][0], ':', top5[i][1], sep = '')
```

Этот скрипт стал итогом работы над ЛР3 и ЛР4, здесь я обьединил все свои наработки, начиная с чтения текста, его нормализацией, токенизацией и написанием отчета. Далее я приложу тест кейсы:

A:
![testA](https://github.com/user-attachments/assets/c05ea5e3-aae3-49e6-b5c4-f477fd6a9f55)
Содержимое csv:
```
word,count
привет,2
мир,1
```
B:
![testB](https://github.com/user-attachments/assets/d2ecc7d5-ac62-4d7f-bfa5-986924372c9a)
Содержимое csv:
```
word,count

```
C:
![testC](https://github.com/user-attachments/assets/67dc094c-e1d0-4f35-b945-e7e2f6edd9db)
Содержимое csv:
```
word,count
привет,1
```
## Лабораторная_05</h1>
### Задание А
```python
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str):
    try:
        path_j = Path(json_path)
        path_c = Path(csv_path)
        with path_j.open('r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError("Пустой JSON или неподдерживаемая структура")
        if data == []:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        fieldnames = data[0].keys()
        with path_c.open('w', newline='', encoding='utf-8') as cf:
            writer = csv.DictWriter(cf, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        print('FileNotFoundError')

def csv_to_json(csv_path: str, json_path: str):
    try:
        path_j = Path(json_path)
        path_c = Path(csv_path)
        with open(path_c, encoding='utf-8') as f:
                try:
                    data = list(csv.DictReader(f))
                except csv.Error:
                    raise ValueError
        if data == []:
            raise ValueError
        with path_j.open('w', encoding='utf-8') as f_j:
            json.dump(data, f_j, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        print('FileNotFoundError')

json_to_csv('C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\samples\\people.json',
            'C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\out\\people_from_json.csv')
csv_to_json('C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\samples\\people.csv', 
            'C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\out\\people_from_csv.json')
```

В этом модуле реализуется две функции, одна переводит json в csv, другая csv в json, о каждой расскажу отдельно.

1)Чтобы перевести json в csv, подключим библиотеки json, csv и pathlib, имея пути ко всем необходимым файлам, подымем ошибку, если их не существует (питон и так ее выводит, но поскольку это отдельно прописано в задании, я решил это прописать). Считаем данные из json при помощи json.load(), не забываю выводить ValueError, если json пуст или с ним что-то не так. Затем открываем csv файл и записываем в него данные из json при помощи csv.DictWriter. Заголовки получаю, когда нахожу ключи в любом словаре из json. Далее приведу скриншоты использования и результаты.

Содержимое people.json:
```
[
  {"name": "Alice", "age": 22},
  {"name": "Bob", "age": 25}
]
```
Содержимое people_from_json.csv, после работы программы:
```
name,age
Alice,22
Bob,25
```
Как видно, данные сохранились с правильным заголовком, верным количеством строк и столбцов.

Пустой json:
<img width="2160" height="1342" alt="blank_json" src="https://github.com/user-attachments/assets/5a16e658-8fe0-4422-a18d-30c1b9725f18" />

Список с не-словарями:
json:
```
[
  (12, 12), (12, 12)
]
```
<img width="2159" height="1439" alt="incorrct_json" src="https://github.com/user-attachments/assets/1cca6439-3edb-4dc7-bca8-7ad21c7545cd" />

2)Чтобы перевести csv в json, используем те же библиотеки. Учитываем ошибки ненахождения файла, а так же чтения csv. Не забываем про то, что если csv файл пуст, необходимо вывести ошибку. Затем просто записываем данные в json при помощи json.dump.

Содержимое people.csv:
```
Имя,Возраст,Город,Профессия
Анна,28,Москва,Инженер
Иван,34,Санкт-Петербург,Дизайнер
```
Содержимое people_from_csv.json после работы программы:
```
[
  {
    "Имя": "Анна",
    "Возраст": "28",
    "Город": "Москва",
    "Профессия": "Инженер"
  },
  {
    "Имя": "Иван",
    "Возраст": "34",
    "Город": "Санкт-Петербург",
    "Профессия": "Дизайнер"
  }
]
```
Ошибка в случае открытие пустого csv:
<img width="2160" height="1440" alt="blank_csv" src="https://github.com/user-attachments/assets/cc145116-1a35-4a36-aa94-bc6d27a0fa47" />

Ошибка, если файла отсутствует:
<img width="2160" height="1440" alt="csv_not_found" src="https://github.com/user-attachments/assets/87824130-ae9e-4c74-93ba-7f18d676da87" />

### Задание B
```python
import csv
from pathlib import Path
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        path_c = Path(csv_path)
        path_x = Path(xlsx_path)
    except FileNotFoundError:
        raise FileNotFoundError
    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'
    with open(path_c, encoding='utf-8') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(path_x)


csv_to_xlsx('C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\samples\\people.csv',
            'C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\out\\people.xlsx')
```
Чтобы переместить данные из csv в xlsx, сначала подключаю необходимые библиотеки csv и openpyxl (предварительно скачав последнюю при помощи pip). Для начала активирую кингу, создаю переменную как первый лист в ней. Теперь в самой функции, ищем файлы по путям, не забывая про ошибку FileNotFoundError. Затем открываем csv файл и построчно добавляем оттуда данные в лист из xlsx. В конце сохраняем файл xlsx.

Содержимое people.csv:
```
Имя,Возраст,Город,Профессия
Анна,28,Москва,Инженер
Иван,34,Санкт-Петербург,Дизайнер
```

Содержимое people.xlsx после работы программы:
<img width="2160" height="1440" alt="exel" src="https://github.com/user-attachments/assets/45dc7a91-4e46-44cc-ab96-59171f2f2a76" />
Можем заметить, что перенос данных произошел корректно.

## Лабораторная_06</h1>
### Номер A
```python
import argparse
from pathlib import Path
from src.lib.text import top_n, normalize, tokenize


def main():
    parser = argparse.ArgumentParser(description='Модуль CLI_text, выводит текст и статистику по нему.')
    subparsers = parser.add_subparsers(dest='command')

    # подкоманда stats
    stats_parser = subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument('--input', required=True, help='Расположение файла')
    stats_parser.add_argument('--top', type=int, default=5, help='Сколько слов выводить в топе')

    # подкоманда cat
    cat_parser = subparsers.add_parser('cat', help='Выводит содержимое файла')
    cat_parser.add_argument('--input', required=True, help='Расположение файла')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    args = parser.parse_args()

    if args.command == 'cat':
        file_path = Path(args.input)
        text = file_path.read_text(encoding='utf-8')
        text = normalize(text, True, True) 
        text_tokens = tokenize(text)
        if args.n:
            for i in range(len(text_tokens)):
                print(text_tokens[i])
        else:
            for i in range(len(text_tokens)):
                print(i, text_tokens[i])
    
    if args.command == 'stats':
        file_path = Path(args.input)
        text = file_path.read_text(encoding='utf-8')
        text = normalize(text, True, True)
        text_tokens = tokenize(text)
        text_top = top_n(text_tokens, args.top)
        for i in range(len(text_top)):
            print(text_top[i])

if __name__ == "__main__":
    main()
```

Для начала, я создаю парсер аргументов, а так же подпарсеры для cat и stats, снабдил их дополнительной информацией в help. Для подкоманды stats я добавил два аргумента: обязательный --input для указания файла и опциональный --top для ограничения количества выводимых слов (по умолчанию 5). Для подкоманды cat я также добавил --input и флаг -n для нумерации строк. В случае если задействуется команда cat, программа читает файл по указанному пути, токенезирует его, и взависимости от n выводит все токены либо пронумерованными, либо - нет. В случае когда исполнить нужно команду stats, текст из указанного файла так же проходит через нормализацию и токенизацию, но затем прогоняется через функцию top_n, после нее слова выводятся по порядку.

Примеры проверки --help:

<img width="621" height="203" alt="cli_text_help_01" src="https://github.com/user-attachments/assets/f9542104-07ac-41c3-bcb4-a649394e51d0" />
![cli_text_help_02](https://github.com/user-attachments/assets/9c5678db-148e-4147-8947-86ac43059d66)
![cli_text_help_03](https://github.com/user-attachments/assets/76d03a59-2a73-48fe-a153-7f5aaf650e8f)

Содержимое text.txt:
```
Привет мир 
Привет Лена
Мир большой
```
Вывод:

![text_output](https://github.com/user-attachments/assets/0b81d491-a1b4-4d34-826d-6372033f48f3)


### Номер B
```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.cvs_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help='конвертация .json в .csv')
    p1.add_argument("--input", dest="input", required=True, help='путь к файлу json')
    p1.add_argument("--output", dest="output", required=True, help='путь к файлу csv')

    p2 = sub.add_parser("csv2json", help='конвертация .csv в .json')
    p2.add_argument("--input", dest="input", required=True, help='путь к файлу csv')
    p2.add_argument("--output", dest="output", required=True, help='путь к файлу json')

    p3 = sub.add_parser("csv2xlsx", help='конвертация .csv в .xlsx')
    p3.add_argument("--input", dest="input", required=True, help='путь к файлу csv')
    p3.add_argument("--output", dest="output", required=True, help='путь к файлу .xlsx')

    args = parser.parse_args()

    if args.cmd == 'json2csv':
        json_to_csv(args.input, args.output)
    elif args.cmd == 'csv2json':
        csv_to_json(args.input, args.output)
    elif args.cmd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
```
Для начала создаем парсер и подпарсеры для трех команд, не забываем про --help. Каждый подпарсер строится по одному шаблону, использование подпарсеров для конвертации - тоже. Чтобы произвести конвертацию, мы просто вызываем функцию из прошлой ЛР, с путями для файлов, полученными из командной строки.

Пример проверки --help:

![convert_help](https://github.com/user-attachments/assets/292fd3c1-9901-486c-b13b-19a0e4323b0b)

Содержимое people.json:
```
[
  {"name": "Alice", "age": 22},
  {"name": "Bob", "age": 25}
]
```
Содержимое people_from_json.csv после работы программы:
```
name,age
Alice,22
Bob,25
```
Содержимое people.csv:
```
Имя,Возраст,Город,Профессия
Анна,28,Москва,Инженер
Иван,34,Санкт-Петербург,Дизайнер
```
Содержимое people_from_csv.json после работы программы:
```
[
  {
    "Имя": "Анна",
    "Возраст": "28",
    "Город": "Москва",
    "Профессия": "Инженер"
  },
  {
    "Имя": "Иван",
    "Возраст": "34",
    "Город": "Санкт-Петербург",
    "Профессия": "Дизайнер"
  }
]
```
Содержимое people.xlsx после работы программы:
![people_xlsx](https://github.com/user-attachments/assets/6e1a25a7-b333-4b0b-8953-4260f36dc0dc)

## Лабораторная_07</h1>
### Задание А
```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "source, casefold, yo2e, expected",
    [
        # базовые случаи с casefold=True и yo2e=True
        ("ПрИвЕт\nМИр\t", True, True, "привет мир"),
        ("ёжик, Ёлка", True, True, "ежик, елка"),
        ("Hello\r\nWorld", True, True, "hello world"),
        ("  двойные   пробелы  ", True, True, "двойные пробелы"),
        # без casefold
        ("ПрИвЕт\nМИр\t", False, True, "ПрИвЕт МИр"),
        ("Hello\r\nWorld", False, True, "Hello World"),
        # без замены ё на е
        ("ёжик, Ёлка", True, False, "ёжик, ёлка"),
        ("Мой Ёж", True, False, "мой ёж"),
        # граничные случаи
        ("", True, True, ""),
        ("   ", True, True, ""),
        ("\n\t\r\b", True, True, ""),
        # комбинации параметров
        ("ПРИВЕТ\nмир\t", False, False, "ПРИВЕТ мир"),
        ("ЁЖИК\nёлка", False, True, "ЕЖИК елка"),
    ],
)
def test_normalize_basic(source, casefold, yo2e, expected):
    assert normalize(source, casefold, yo2e) == expected

@pytest.mark.parametrize(
    "source, expected",
    [
        # базовые случаи
        ("Привет, мир!", ["Привет", "мир"]),
        ("Hello world!", ["Hello", "world"]),
        # граничные случаи
        ("", []),
        ("!#$%", []),
        ("   ", []),
        # спецсимволы
        ("Вопрос? Ответ! Итог:", ["Вопрос", "Ответ", "Итог"]),
        ("Цена: $100 & 50% скидка", ["Цена", "100", "50", "скидка"]),
        # эмодзи и тире
        ("Я 😀 счастлив!", ["Я", "счастлив"]),
        ("Длинное — очень длинное тире", ["Длинное", "очень", "длинное", "тире"]),
        # много разделители
        ("Слово,,, слово!!! слово???", ["Слово", "слово", "слово"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected

@pytest.mark.parametrize(
    "tokens, expected",
    [
        # базовые тесты для count_freq
        (
            ["я", "люблю", "python", "я", "люблю", "код"],
            {"я": 2, "код": 1, "люблю": 2, "python": 1},
        ),
        (["test"], {"test": 1}),
        (["word", "word", "word"], {"word": 3}),
    ],
)
def test_count_f_basic(tokens, expected):
    assert count_freq(tokens) == expected

@pytest.mark.parametrize(
    "tokens, n, expected",
    [
        # базовые тесты для top_n
        (
            ["я", "люблю", "python", "я", "люблю", "код", "python", "python"],
            2,
            [("python", 3), ("люблю", 2)],
        ),
        (["a", "b", "a"], 5, [("a", 2), ("b", 1)]),
        ([], 5, []),
        # случай с одинаковой частотой, для проверки сортировки по алфавиту
        (
            ["яблоко", "апельсин", "яблоко", "апельсин", "банан", "банан"],
            3,
            [("апельсин", 2), ("банан", 2), ("яблоко", 2)],
        ),
        (
            ["z", "a", "b", "z", "a", "c", "b", "a", "d"],
            4,
            [("a", 3), ("b", 2), ("z", 2), ("c", 1)],
        ),
    ],
)
def test_top_n_basic(tokens, n, expected):
    assert top_n(tokens, n) == expected
```
В начале работы я устанавливаю pytest при помощи pip, после этого проверяю установку black. Затем, при помощи параметризации, я создаю набор тестов для каждой функции. Для normalize мне необходимо было проверить механизмы замены ё на е, схлопывания пробелов, реакцию функции на пустые строки, и строки, состоящие из служебных символов. Для функции tokenize, после базовых проверок работы, необходимо было проверить случаи со множеством символов разделителей, спецсимволов и эмодзи. Функцию count_freq я проверял базовыми последовательностями и перемешиваниями слов. top_n я тестировал при помощи базовых последовательностей символов, однако отдельно вынес тесты для проверки работы сортировки по алфавиту.
![text_pytest](https://github.com/user-attachments/assets/856e50cf-e88a-4881-94bb-8baab31cc681)
Так же, я проверил оформление кода при помощи black:
![text_black](https://github.com/user-attachments/assets/dc49cbb7-7265-4352-b15a-073c1931f3bf)

### Задание B
```python
import pytest
import csv
import json
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json

def test_json_to_csv_roundtrip(tmp_path: Path):
    # базовый тест конвертации json
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "22"
    assert rows[1]["name"] == "Bob"
    assert rows[1]["age"] == "25"


def test_csv_to_json_roundtrip(tmp_path: Path):
    # базовый тест конвертации csv
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    # создаем CSV файл
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(
            [
                {"name": "Alice", "age": "22"},
                {"name": "Bob", "age": "25"},
            ]
        )

    csv_to_json(str(src), str(dst))
    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[0]["age"] == "22"
    assert data[1]["name"] == "Bob"
    assert data[1]["age"] == "25"


def test_json_to_csv_empty_json(tmp_path: Path):
    # тест обработки пустого json
    src = tmp_path / "empty.json"
    dst = tmp_path / "output.csv"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="Пустой JSON или неподдерживаемая структура"):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_csv(tmp_path: Path):
    # тест обработки пустого csv
    src = tmp_path / "empty.csv"
    dst = tmp_path / "output.json"

    # cоздаем CSV только с заголовком
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_file_not_found(tmp_path: Path, capsys):
    # тест на FileNotFoudError
    src = tmp_path / "nonexistent.json"
    dst = tmp_path / "output.csv"

    json_to_csv(str(src), str(dst))

    captured = capsys.readouterr()
    assert "FileNotFoundError" in captured.out
```
В случае с тестом для функций, работающих с файлами, необходимо использовать tmp_path, чтобы не городить ненужные файлы в \data. Я начал с базовых тестов конвертации json в csv, там я проверил соответствие значений в ячейках, количество строк. Затем похожий базовый тест для конвертации csv в json. Далее необходимо было проверить работу функций с пустыми файлами. Завершает тесты проверка ошибки FileNotFoundError. (проверка black в скриншоте)
![json_text_black](https://github.com/user-attachments/assets/31bfb3d2-d4c7-4416-89ee-76d611d8a17a)

## Лабораторная_08</h1>
### Задание А
```python
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        #валидация даты рождения
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Некорректный формат даты")
        
        #валидация среднего балла
        if not (0 <= self.gpa <= 5):
            raise ValueError("Средний балл должен быть в диапазоне 0-5")
        
        #валидация ФИО
        if not self.fio or not self.fio.strip():
            raise ValueError("ФИО не может быть пустым")
        
        #валидация группы
        if not self.group or not self.group.strip():
            raise ValueError("Группа не может быть пустой")
    
    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year #вычисляем возраст
        if (today.month, today.day) < (birth_date.month, birth_date.day): #учитываем месяц и день рождения
            age -= 1
        return age
    
    def to_dict(self) -> Dict[str, Any]: #cериализация объекта в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student': #десериализация объекта из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str: #вывод информации о студенте
        return f"Студент: {self.fio}, Группа: {self.group}, Возраст: {self.age()}, Средний балл: {self.gpa}"
```
Для начала создаем класс Student с необходимыми полями, затем проводим валидацию всех данных через функцию __post_init__, затем создаем метод age при помощи библиотеки datetime. Сериализация и десериализация проходят при помощи функций to_dict и from_dict соответственно. Не забываем про крассивый вывод при помощи __str__.
### Задание В
```python
import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students] #сериализуем студентов в словари
    with open(path, 'w', encoding='utf-8') as f: #записываем в файл
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    students = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив объектов")
        # Создаем объекты Student и валидируем их
        for i, item in enumerate(data):
            try:
                # Проверяем наличие всех необходимых полей
                required_fields = ['fio', 'birthdate', 'group', 'gpa']
                for field in required_fields:
                    if field not in item:
                        raise ValueError(f"Отсутствует обязательное поле: {field}")
                student = Student.from_dict(item)
                students.append(student)
            except ValueError as e:
                print(f"Ошибка при обработке записи {i}: {e}")
                continue
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON файла: {path}")
        return []
    return students

#тестовый запуск
students = students_from_json("C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\lab08\\students_input.json")
students_to_json(students, 'C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\lab08\\students_output.json')
for i in range(len(students)):
    print(students[i])
```
Сначала реализовываем функцию students_to_json, она записывает данные в файл json, используя to_dict из предыдущего задания. Функция students_from_json сложнее, она дополнительно к записи из файла проводит валидацию данных. Так же я ипользовал функцию List из библиотеки typing, для более удобной работы со списками. В конце прописан код для тестового запуска.

### Тестовый запуск
Содержимое students_input.json:
```
[
    {"fio": "Иванов Иван", "birthdate": "2000-03-15", "group": "SE-01", "gpa": 4.2},
    {"fio": "Петров Петр", "birthdate": "2001-07-22", "group": "SE-02", "gpa": 3.8},
    {"fio": "Сидорова Анна", "birthdate": "1999-11-30", "group": "CS-01", "gpa": 4.9}
]
```

Содержимое students_output.json:
```
[
  {
    "fio": "Иванов Иван",
    "birthdate": "2000-03-15",
    "group": "SE-01",
    "gpa": 4.2
  },
  {
    "fio": "Петров Петр",
    "birthdate": "2001-07-22",
    "group": "SE-02",
    "gpa": 3.8
  },
  {
    "fio": "Сидорова Анна",
    "birthdate": "1999-11-30",
    "group": "CS-01",
    "gpa": 4.9
  }
]
```
Скриншот запуска:
<img width="2159" height="1345" alt="lab08_test" src="https://github.com/user-attachments/assets/c027ef77-1851-480f-b0d7-ca7ecad0247b" />
