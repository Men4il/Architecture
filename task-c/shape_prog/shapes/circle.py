import math
import random
from typing import List, Optional

from shape_prog.shapes.base import BaseShape
from shape_prog.common.exceptions import NotEnoughTokensError, TooManyTokensError


class Circle(BaseShape):
    def __init__(self):
        super().__init__()
        self._x: Optional[int] = None
        self._y: Optional[int] = None
        self._radius: Optional[float] = None

    def __repr__(self):
        return f"It is Circle: color is {self.color} " \
               f"center coordinates = x: {self.center_x}, y: {self.center_y}. " \
               f"radius = {self.radius:.3f}, square = {self.square}"

    @property
    def center_x(self):
        return self._x

    @center_x.setter
    def center_x(self, value):
        self._x = value

    @property
    def center_y(self):
        return self._y

    @center_y.setter
    def center_y(self, value):
        self._y = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def square(self) -> float:
        """Нахождение площади фигуры"""
        return self.radius * self.radius * math.pi

    def rand_fill(self):
        super().rand_fill()
        self._x = random.randint(-1000, 1000)
        self._y = random.randint(-1000, 1000)
        self.radius = random.randint(-250, 250)

    def str_fill(self, tokens: List[str]):
        """Заполняет информацию о фигуре"""
        if len(tokens) < 3:
            raise NotEnoughTokensError("Not enough tokens, for circle, it is necessary to have 3 parameters: "
                                       "center x, center y and radius")
        elif len(tokens) == 3:
            self._x = int(tokens[0])
            self._y = int(tokens[1])
            self._radius = int(tokens[2])

        else:
            raise TooManyTokensError("Too many tokens, for circle, it is necessary to have 3 parameters: "
                                     "center x, center y and radius")
