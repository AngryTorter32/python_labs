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
        # Валидация даты рождения
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Некорректный формат даты")
        
        # Валидация среднего балла
        if not (0 <= self.gpa <= 5):
            raise ValueError("Средний балл должен быть в диапазоне 0-5")
        
        # Валидация ФИО (не должно быть пустым)
        if not self.fio or not self.fio.strip():
            raise ValueError("ФИО не может быть пустым")
        
        # Валидация группы (не должна быть пустой)
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
