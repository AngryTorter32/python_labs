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
