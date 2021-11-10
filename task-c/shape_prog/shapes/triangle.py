import random
from typing import List, Optional

from shape_prog.shapes.base import BaseShape
from shape_prog.common.exceptions import NotEnoughTokensError, TooManyTokensError


class Triangle(BaseShape):
    def __init__(self):
        super().__init__()
        self._first_x: Optional[int] = None
        self._first_y: Optional[int] = None
        self._second_x: Optional[int] = None
        self._second_y: Optional[int] = None
        self._third_x: Optional[int] = None
        self._third_y: Optional[int] = None

    def __repr__(self):
        return f"It is Triangle: color is {self.color} " \
               f"first corner = x: {self.first_x}, y: {self.first_y}. " \
               f"second corner = x: {self.second_x}, y: {self.second_y}. " \
               f"third corner = x: {self.third_x}, y: {self.third_y}. " \
               f"square = {self.square}"

    @property
    def first_x(self):
        return self._first_x

    @first_x.setter
    def first_x(self, value):
        self._first_x = value

    @property
    def first_y(self):
        return self._first_y

    @first_y.setter
    def first_y(self, value):
        self._first_y = value

    @property
    def second_x(self):
        return self._second_x

    @second_x.setter
    def second_x(self, value):
        self._second_x = value

    @property
    def second_y(self):
        return self._second_y

    @second_y.setter
    def second_y(self, value):
        self._second_y = value

    @property
    def third_x(self):
        return self._third_x

    @third_x.setter
    def third_x(self, value):
        self._third_x = value

    @property
    def third_y(self):
        return self._third_y

    @third_y.setter
    def third_y(self, value):
        self._third_y = value

    @property
    def square(self) -> float:
        """Нахождение площади фигуры"""
        temp = (self.second_x - self.first_x) * (self.third_y - self.first_y) - \
               (self.third_x - self.first_x) * (self.second_y - self.first_y)

        if temp < 0:
            return temp * -1
        else:
            return temp

    def rand_fill(self):
        super().rand_fill()
        self._first_x = random.randint(-1000, 1000)
        self._first_y = random.randint(-1000, 1000)
        self._second_x = random.randint(-1000, 1000)
        self._second_y = random.randint(-1000, 1000)
        self._third_x = random.randint(-1000, 1000)
        self._third_y = random.randint(-1000, 1000)

    def str_fill(self, tokens: List[str]):
        """Заполняет информацию о фигуре"""
        if len(tokens) < 6:
            raise NotEnoughTokensError("Not enough tokens, for triangle, it is necessary to have 6 parameters: "
                                       "first corner x and y, second corner x and y, third corner x and y")
        elif len(tokens) == 6:
            self._first_x = int(tokens[0])
            self._first_y = int(tokens[1])
            self._second_x = int(tokens[2])
            self._second_y = int(tokens[3])
            self._third_x = int(tokens[4])
            self._third_y = int(tokens[5])

        else:
            raise TooManyTokensError("Too many tokens, for triangle, it is necessary to have 6 parameters: "
                                     "first corner x and y, second corner x and y, third corner x and y")
