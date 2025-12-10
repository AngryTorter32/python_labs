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

    # читаем и проверяем JSON
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
