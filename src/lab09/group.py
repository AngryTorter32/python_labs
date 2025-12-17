import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student



class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])

    def _read_all(self) -> List[dict]:
        rows = []
        if self.path.exists():
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        row['gpa'] = float(row['gpa'])
                        rows.append(row)
                    except ValueError:
                        continue
        return rows

    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=row['gpa']
                )
                students.append(student)
            except KeyError:
                continue
        return students

    def add(self, student: Student):
        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                student.gpa
            ])

    def find(self, substr: str) -> List[Student]:
        all_students = self.list()
        return [student for student in all_students if substr.lower() in student.fio.lower()]

    def remove(self, fio: str):
        rows = self._read_all()
        updated_rows = [row for row in rows if row['fio'] != fio]
        
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
            for row in updated_rows:
                writer.writerow([row['fio'], row['birthdate'], row['group'], row['gpa']])

    def update(self, fio: str, **fields):
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for field, value in fields.items():
                    if field == 'gpa':
                        row[field] = float(value)
                    else:
                        row[field] = value
                updated = True
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
            for row in rows:
                writer.writerow([row['fio'], row['birthdate'], row['group'], row['gpa']])


def main():
    #Тестовый запуск
    csv_file_path = "C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\lab09\\students.csv"
    
    group = Group(csv_file_path)
    
    print("Чтение всех студентов из файла:")
    students = group.list()
    
    if students:
        print(f"Найдено студентов: {len(students)}")
        for i, student in enumerate(students, 1):
            print(f"{i:2}. {student}")
    else:
        print("В файле нет записей студентов (только заголовки)")

    print()
    print("Поиск студентов по подстроке 'Иванов':")
    found_students = group.find("Иванов")
    if found_students:
        for i, student in enumerate(found_students, 1):
            print(f"{i:2}. {student}")
    else:
        print("Студенты с такой подстрокой не найдены")
    
    print()
    print("Добавление нового студента:")
    try:
        new_student = Student(
            "Иванов Сергей Петрович",
            "2002-05-15",
            "ИС-104",
            4.3
        )
        group.add(new_student)
        print(f"Добавлен: {new_student}")
    except Exception as e:
        print(f"Ошибка при добавлении: {e}")
    
    print()
    print("Обновление данных студента:")
    if students:
        first_student_fio = students[0].fio
        try:
            print(f"Обновляем данные для: {first_student_fio}")
            print("Изменяем группу на 'ИС-105' и GPA на 4.7")
            group.update(first_student_fio, group="ИС-105", gpa=4.7)
            print("Данные успешно обновлены")
        except ValueError as e:
            print(f"Ошибка: {e}")
    else:
        print("Нет студентов для обновления")
    
    print()
    print("Удаление студента:")
    test_fio = "Несуществующий Студент"
    print(f"Попытка удалить: '{test_fio}'")
    initial_count = len(group.list())
    group.remove(test_fio)
    final_count = len(group.list())
    if initial_count == final_count:
        print(f"Студент не найден, количество записей не изменилось: {final_count}")
    else:
        print(f"Студент удален. Было: {initial_count}, стало: {final_count}")
    
    print()
    print("Итоговый список студентов:")
    final_students = group.list()
    if final_students:
        for i, student in enumerate(final_students, 1):
            print(f"{i:2}. {student}")
        print(f"Всего студентов: {len(final_students)}")
    else:
        print("Нет записей студентов")
    
    print()
    print("Файл сохранен с изменениями.")

if __name__ == "__main__":
    main()
