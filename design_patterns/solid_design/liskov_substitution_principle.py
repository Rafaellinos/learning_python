# LSP
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self._width}, height: {self._height}'

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)


"""
sq output:
Expected an area of 20, got 20
Expected an area of 50, got 100

Quebra o principio de liskov, o método use_it
deveria funcionar da mesma maneira.
"""