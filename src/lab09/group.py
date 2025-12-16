import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        """Инициализация группы и файла-хранилища"""
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создать файл с заголовком, если его ещё нет"""
        if not self.path.exists():
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])

    def _read_all(self) -> List[dict]:
        """Прочитать все строки из CSV"""
        rows = []
        if self.path.exists():
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Преобразуем gpa в float, так как CSV хранит строки
                    row['gpa'] = float(row['gpa'])
                    rows.append(row)
        return rows

    def list(self) -> List[Student]:
        """Вернуть всех студентов в виде списка Student"""
        rows = self._read_all()
        students = []
        for row in rows:
            student = Student(
                fio=row['fio'],
                birthdate=row['birthdate'],
                group=row['group'],
                gpa=row['gpa']
            )
            students.append(student)
        return students

    def add(self, student: Student):
        """Добавить нового студента в CSV"""
        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                student.gpa
            ])

    def find(self, substr: str) -> List[Student]:
        """Найти студентов по подстроке в fio"""
        all_students = self.list()
        return [student for student in all_students if substr.lower() in student.fio.lower()]

    def remove(self, fio: str):
        """Удалить запись(и) с данным fio"""
        rows = self._read_all()
        # Удаляем все записи с указанным ФИО
        updated_rows = [row for row in rows if row['fio'] != fio]

        # Записываем обновленные данные обратно в файл
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
            for row in updated_rows:
                writer.writerow([row['fio'], row['birthdate'], row['group'], row['gpa']])

    def update(self, fio: str, **fields):
        """Обновить поля существующего студента"""
        rows = self._read_all()
        updated = False

        for row in rows:
            if row['fio'] == fio:
                # Обновляем только указанные поля
                for field, value in fields.items():
                    if field == 'gpa':
                        # Преобразуем gpa обратно в строку для записи
                        row[field] = float(value)
                    else:
                        row[field] = value
                updated = True

        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")

        # Записываем обновленные данные обратно в файл
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
            for row in rows:
                writer.writerow([row['fio'], row['birthdate'], row['group'], row['gpa']])