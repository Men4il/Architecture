import random
import time
from abc import ABC
from collections import Sequence
from pathlib import Path
from typing import Optional, Union, List

from shape_prog.shapes.circle import Circle
from shape_prog.common.exceptions import NotEnoughTokensError
from shape_prog.shapes.triangle import Triangle
from shape_prog.shapes.rectangle import Rectangle
from shape_prog.shapes.shapes import ShapeType


class Container(Sequence, ABC):
    """Класс контейнера фигуры"""
    def __init__(self, filename: Optional[str] = None, n_random: Optional[int] = None):
        self.shapes: List[Union[Rectangle]] = []
        if filename:
            for line in Path(filename).read_text().splitlines():
                shape = self.read_shape_from_str(line)
                self.shapes.append(shape)
        elif n_random:
            if type(n_random) == str:
                n_random = int(n_random)
            for _ in range(n_random):
                shape = self.rand_shape()
                self.shapes.append(shape)
        self.start_time = time.time()

    def __len__(self):
        return len(self.shapes)

    def __getitem__(self, item):
        return self.shapes[item]

    @staticmethod
    def rand_shape() -> Union[Circle, Rectangle, Triangle]:
        """Генерация случайной фигуры"""
        type_shape = random.choice([item.value for item in ShapeType])
        shape = None
        if ShapeType(type_shape) == ShapeType.RECTANGLE:
            shape = Rectangle()
        elif ShapeType(type_shape) == ShapeType.TRIANGLE:
            shape = Triangle()
        elif ShapeType(type_shape) == ShapeType.CIRCLE:
            shape = Circle()
        shape.rand_fill()
        return shape

    @staticmethod
    def read_shape_from_str(line: str) -> Union[Circle, Rectangle, Triangle]:
        """Ввод фигуры из строки с её описанием"""
        tokens = line.split()
        if len(tokens) < 2:
            raise NotEnoughTokensError("Base shape must contain at least 2 tokens: "
                                       "shape and color")
        shape_type = tokens[0]
        shape = None
        if ShapeType(shape_type) == ShapeType.RECTANGLE:
            shape = Rectangle()
        elif ShapeType(shape_type) == ShapeType.TRIANGLE:
            shape = Triangle()
        elif ShapeType(shape_type) == ShapeType.CIRCLE:
            shape = Circle()
        shape.color = tokens[1]
        shape.str_fill(tokens=tokens[2:])
        return shape

    def sort(self):
        """Сортирует контейнер по площадям фигур"""
        i = 0
        while i < len(self.shapes):
            k = i
            for j in range(i + 1, len(self.shapes)):
                if self.shapes[j].square > self.shapes[k].square:
                    k = j
            self.shapes[i], self.shapes[k] = self.shapes[k], self.shapes[i]
            i += 1
