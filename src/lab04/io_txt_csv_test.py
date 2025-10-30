from pathlib import Path
import csv
from typing import Iterable, Sequence

'''
def read_text(path: str | Path, encoding: str = "utf-8") -> str: # FileNotFoundError и UnicodeDecodeError могут появляться
    p = Path(path)
    return p.read_text(encoding=encoding)
file_name = input('Введите название файла в папке data (по умолчанию - input.txt): ')
if file_name == '':
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt" #по умолчанию используется файл input.txt
else:
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04" + f'\{file_name}'
cod = input('Введите кодировку файла (по умолчанию - utf-8): ') #по желанию пользователя, может быть выбрана другая кодировка
if cod == '':
    cod = 'utf-8' #по умолчанию кодировка utf-8
print(read_text(r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt", 'utf-8')) #пользователь может выбрать другую кодировку или расположения файла, если изменит их при запуске программы
'''

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
write_csv([("Проект А", "100000", "80000", "20000"), ("Проект Б", "50000", "45000", "5000"), ("Проект В", "75000", "60000", "15000")], Path("C:/Users/kuzne/Desktop/laby_piton/python_labs/src/data/lab04/input.txt"), ("Проект", "Доход", "Расход", "Прибыль"))