class Shape:
    def __init__(self):
        self._width = 0
        self._height = 0

    def get_width(self):
        return self._width
    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height
    def set_height(self, value):
        self._height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)

class Rectangle(Shape):
    pass


class Square(Shape):
    def get_width(self):
        return self._width
    def set_width(self, value):
        if((value != self._height) and (self._width != 0)):
            raise Exception("Width and Height for Square can't be different")
        else:
            self._width = value
            self._height = value

    def get_height(self):
        return self._height
    def set_height(self, value):
        if((value != self._width) and (self._height != 0)):
            raise Exception("Width and Height for Square can't be different")
        else:
            self._width = value
            self._height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)

from typing import List

class AreaCalculator:
    def calculateArea(self, shapes: List[Shape]):
        for shape in shapes:
            print(f"Area : {shape.width * shape.height}")


class Line:
    def __init__(self, length):
        self.length = length


class Box:
    """
    Duck Typing 
      - Box is similar to Shape class but it is not inheriting it.
      - while calculating area it does not check the class type,
        it only do the function if the object has width and height

    If anything(not a duck) walk, talk like a duck, then it is duck
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height


sq = Square()
sq.width = 10

rect = Rectangle()
rect.width = 10
rect.height = 5

box = Box(10,20)

shapes = [sq, rect, box]
AreaCalculator().calculateArea(shapes)