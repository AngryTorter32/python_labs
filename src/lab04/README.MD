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
