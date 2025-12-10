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
