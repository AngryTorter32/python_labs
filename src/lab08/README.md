## Лабораторная_08</h1>
### Задание А
```python
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        #валидация даты рождения
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Некорректный формат даты")
        
        #валидация среднего балла
        if not (0 <= self.gpa <= 5):
            raise ValueError("Средний балл должен быть в диапазоне 0-5")
        
        #валидация ФИО
        if not self.fio or not self.fio.strip():
            raise ValueError("ФИО не может быть пустым")
        
        #валидация группы
        if not self.group or not self.group.strip():
            raise ValueError("Группа не может быть пустой")
    
    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year #вычисляем возраст
        if (today.month, today.day) < (birth_date.month, birth_date.day): #учитываем месяц и день рождения
            age -= 1
        return age
    
    def to_dict(self) -> Dict[str, Any]: #cериализация объекта в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student': #десериализация объекта из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str: #вывод информации о студенте
        return f"Студент: {self.fio}, Группа: {self.group}, Возраст: {self.age()}, Средний балл: {self.gpa}"
```
Для начала создаем класс Student с необходимыми полями, затем проводим валидацию всех данных через функцию __post_init__, затем создаем метод age при помощи библиотеки datetime. Сериализация и десериализация проходят при помощи функций to_dict и from_dict соответственно. Не забываем про крассивый вывод при помощи __str__.
### Задание В
```python
import json
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students] #сериализуем студентов в словари
    with open(path, 'w', encoding='utf-8') as f: #записываем в файл
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
                student = Student.from_dict(item)
                students.append(student)
            except ValueError as e:
                print(f"Ошибка при обработке записи {i}: {e}")
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
```
Сначала реализовываем функцию students_to_json, она записывает данные в файл json, используя to_dict из предыдущего задания. Функция students_from_json сложнее, она дополнительно к записи из файла проводит валидацию данных. Так же я ипользовал функцию List из библиотеки typing, для более удобной работы со списками. В конце прописан код для тестового запуска.

### Тестовый запуск
Содержимое students_input.json:
```
[
    {"fio": "Иванов Иван", "birthdate": "2000-03-15", "group": "SE-01", "gpa": 4.2},
    {"fio": "Петров Петр", "birthdate": "2001-07-22", "group": "SE-02", "gpa": 3.8},
    {"fio": "Сидорова Анна", "birthdate": "1999-11-30", "group": "CS-01", "gpa": 4.9}
]
```

Содержимое students_output.json:
```
[
  {
    "fio": "Иванов Иван",
    "birthdate": "2000-03-15",
    "group": "SE-01",
    "gpa": 4.2
  },
  {
    "fio": "Петров Петр",
    "birthdate": "2001-07-22",
    "group": "SE-02",
    "gpa": 3.8
  },
  {
    "fio": "Сидорова Анна",
    "birthdate": "1999-11-30",
    "group": "CS-01",
    "gpa": 4.9
  }
]
```
Скриншот запуска:
<img width="2159" height="1345" alt="lab08_test" src="https://github.com/user-attachments/assets/c027ef77-1851-480f-b0d7-ca7ecad0247b" />
