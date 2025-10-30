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
