from datetime import datetime, date
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Student:
    """Класс для представления студента."""
    
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        Валидация данных после инициализации.
        Проверяет формат даты и диапазон GPA.
        """
        # Валидация формата даты (YYYY-MM-DD как в задании)
        try:
            # Используем формат из задания (YYYY-MM-DD)
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            # Поднимаем исключение с понятным сообщением
            raise ValueError(
                f"Неверный формат даты: {self.birthdate}. "
                f"Ожидается формат YYYY-MM-DD (например, 2000-12-31)"
            )
        
        # Валидация диапазона GPA (0...5 как в задании)
        if not (0 <= self.gpa <= 5):
            raise ValueError(
                f"GPA должен быть в диапазоне от 0 до 5. "
                f"Получено: {self.gpa}"
            )

    def age(self) -> int:
        """
        Возвращает количество полных лет студента.
        
        Returns:
            int: Количество полных лет
        """
        # Парсим дату рождения из строки
        # Используем формат YYYY-MM-DD
        birthdate_obj = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем возраст в полных годах
        age_years = today.year - birthdate_obj.year
        
        # Проверяем, был ли уже день рождения в текущем году
        # Сравниваем месяц и день
        if (today.month, today.day) < (birthdate_obj.month, birthdate_obj.day):
            age_years -= 1  # День рождения еще не был в этом году
        
        return age_years

    def to_dict(self) -> Dict[str, Any]:
        """
        Сериализует объект Student в словарь.
        
        Returns:
            Dict[str, Any]: Словарь со всеми полями студента
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> 'Student':
        """
        Десериализует объект Student из словаря.
        
        Args:
            d (Dict[str, Any]): Словарь с данными студента
            
        Returns:
            Student: Новый объект класса Student
        """
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self) -> str:
        """
        Возвращает строковое представление студента.
        
        Returns:
            str: Красиво отформатированная строка с информацией о студенте
        """
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, возраст: {self.age()} лет"
