import random
from typing import List, Optional

from shape_prog.shapes.base import BaseShape
from shape_prog.common.exceptions import NotEnoughTokensError, TooManyTokensError


class Rectangle(BaseShape):
    def __init__(self):
        super().__init__()
        self._left_x: Optional[int] = None
        self._left_y: Optional[int] = None
        self._right_x: Optional[int] = None
        self._right_y: Optional[int] = None

    def __repr__(self):
        return f"It is Rectangle: color is {self.color} " \
               f"left top corner = x: {self.upper_left_x}, y: {self.upper_left_y}. " \
               f"right bottom corner = x: {self.down_right_x}, y: {self.down_right_y}. " \
               f"square = {self.square}"

    @property
    def upper_left_x(self):
        return self._left_x

    @upper_left_x.setter
    def upper_left_x(self, value):
        if self._right_x is None:
            self._left_x = value
        elif value <= self._right_x:
            self._left_x = value
        else:
            raise ValueError(f"Value expected to be in top left corner, but x: \"{value}\" is not")

    @property
    def upper_left_y(self):
        return self._left_y

    @upper_left_y.setter
    def upper_left_y(self, value):
        if self._right_y is None:
            self._left_y = value
        elif value >= self._right_y:
            self._left_y = value
        else:
            raise ValueError(f"Value expected to be in top left corner, but y: \"{value}\" is not")

    @property
    def down_right_x(self):
        return self._right_x

    @down_right_x.setter
    def down_right_x(self, value):
        if self._left_x is None:
            self._right_x = value
        elif value >= self._left_x:
            self._right_x = value
        else:
            raise ValueError(f"Value expected to be in right bottom corner, but x: \"{value}\" is not")

    @property
    def down_right_y(self):
        return self._right_y

    @down_right_y.setter
    def down_right_y(self, value):
        if self._left_y is None:
            self._right_y = value
        elif value <= self._left_y:
            self._right_y = value
        else:
            raise ValueError(f"Value expected to be in right bottom corner, but y: \"{value}\" is not")

    @property
    def square(self) -> float:
        """Нахождение площади фигуры"""
        return (self.upper_left_y - self.down_right_y) * (self.down_right_x - self.upper_left_x)

    def rand_fill(self):
        super().rand_fill()
        self._left_x = random.randint(-1000, 0)
        self._left_y = random.randint(0, 1000)
        self._right_x = random.randint(0, 1000)
        self._right_y = random.randint(-1000, 0)

    def str_fill(self, tokens: List[str]):
        """Заполняет информацию о фигуре"""
        if len(tokens) < 4:
            raise NotEnoughTokensError("Not enough tokens, for rectangle, it is necessary to have 4 parameters: "
                                       "top left x, y and bot right x, y")
        elif len(tokens) == 4:
            self._left_x = int(tokens[0])
            self._left_y = int(tokens[1])
            self._right_x = int(tokens[2])
            self._right_y = int(tokens[3])

        else:
            raise TooManyTokensError("Too many tokens, for rectangle, it is necessary to have 4 parameters: "
                                     "top left x, y and bot right x, y")
