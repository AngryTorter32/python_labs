import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    # Сериализуем студентов в словари
    data = [student.to_dict() for student in students]
    # Записываем в файл
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    students = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив объектов")
        # Создаем объекты Student и валидируем их
        for i, item in enumerate(data):
            try:
                # Проверяем наличие всех необходимых полей
                required_fields = ['fio', 'birthdate', 'group', 'gpa']
                for field in required_fields:
                    if field not in item:
                        raise ValueError(f"Отсутствует обязательное поле: {field}")
                
                # Создаем студента (валидация происходит в __post_init__)
                student = Student.from_dict(item)
                students.append(student)
                
            except ValueError as e:
                print(f"Ошибка при обработке записи {i}: {e}")
                continue
            except Exception as e:
                print(f"Неожиданная ошибка при обработке записи {i}: {e}")
                continue
                
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON файла: {path}")
        return []
    return students

#тестовый запуск
students = students_from_json("C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\lab08\\students_input.json")
students_to_json(students, 'C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\lab08\\students_output.json')
for i in range(len(students)):
    print(students[i])