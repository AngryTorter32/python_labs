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
