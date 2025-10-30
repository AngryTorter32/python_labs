from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str: # FileNotFoundError и UnicodeDecodeError можно не предотвращать
    p = Path(path)
    return p.read_text(encoding=encoding)
file_name = input('Введите название файла в папке data (по умолчанию - input.txt): ') #по желанию пользователя, он может выбрать другой файл в папке
if file_name == '':
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt" #по умолчанию используется файл input.txt
else:
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04" + f'\{file_name}'
cod = input('Введите кодировку файла (по умолчанию - utf-8): ') #по желанию пользователя, может быть выбрана другая кодировка
if cod == '':
    cod = 'utf-8' #по умолчанию кодировка utf-8
print(read_text(file_path, cod))

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