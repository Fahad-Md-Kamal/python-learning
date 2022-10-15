class Rectangle:
    def __init__(self, width=0, height=0) -> None:
        self._width = width
        self._height = height

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


class AreaCalculator:
    def calculateArea(self, rectangles):
        for rectangle in rectangles:
            print(f"Area : {rectangle.width * rectangle.height}")

class Square(Rectangle):
    def get_width(self):
        return self._width
    def set_width(self, value):
        self._width = value
        self._height = value
    
    def get_height(self):
        return self._height
    def set_height(self, value):
        self._height = value
        self._width = value
    
    width = property(get_width, set_width)
    height = property(get_height, set_height)

sq = Square()
sq.width = 10
sq.height = 10

rect = Square()
rect.width = 10
rect.height = 5

shapes = [sq, rect]
ac = AreaCalculator()
ac.calculateArea(shapes)