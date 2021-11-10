import random
from enum import Enum
from typing import Optional


class Color(Enum):
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    CYAN = 'cyan'
    BLUE = 'blue'
    PURPLE = 'purple'


class BaseShape:
    """Базовый класс фигуры"""
    def __init__(self):
        """Конструктор базового класса фигуры, создаёт поля и заполняет их None"""
        self._color: Optional[Enum] = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        """Устанавливает цвет фигуры

        :param value: новое значение

        :raises ValueError: если новое значение не соответствует списку представленых цветов
        """
        if value == 'red':
            self._color = Color.RED
        elif value == 'orange':
            self._color = Color.ORANGE
        elif value == 'yellow':
            self._color = Color.YELLOW
        elif value == 'green':
            self._color = Color.GREEN
        elif value == 'cyan':
            self._color = Color.CYAN
        elif value == 'blue':
            self._color = Color.BLUE
        elif value == 'purple':
            self._color = Color.PURPLE
        else:
            raise ValueError(f"Colors expected to be in given enum list, but \"{value}\" is not supported")

    def rand_fill(self):
        """Заполнение параметров фигуры рандомно"""
        self._color = random.choice(list(Color))
