class Rectangle:
    POINTS = "*"

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    
    def set_width(self, width: int) -> None:
        self._width = width
    
    def set_height(self, height: int) -> None:
        self._height = height
    
    def get_area(self) -> int:
        return self._width * self._height
    
    def get_perimeter(self) -> int:
        return 2 * (self._width + self._height)
    
    def get_diagonal(self) -> float:
        return (self._width ** 2 + self._height ** 2) ** .5
    
    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50: return "Too big for picture."
        return (self.POINTS*self._width + "\n")*self._height
    
    def get_amount_inside(self, shape) -> int:
        """How many times a rectangular shape could fit in this one based on volume"""
        if not isinstance(shape, Rectangle): raise ValueError("Invalid Input")
        return self.get_area()//shape.get_area()
    
    def __repr__(self) -> str:
        rect_string = "{}(width={}, height={})".format(
            self.__class__.__name__,
            self._width,
            self._height
        )
        return rect_string


class Square(Rectangle):
    
    def __init__(self, side: int):
        super().__init__(side, side)
    
    def set_side(self, side: int) -> None:
        self.set_height(side)
        self.set_width(side)
    
    def set_width(self, side: int) -> None:
        super().set_width(side)
        super().set_height(side)
    
    def set_height(self, side: int) -> None:
        super().set_width(side)
        super().set_height(side)
    
    def __repr__(self) -> str:
        sqr_string = "{}(side={})".format(
            self.__class__.__name__,
            self._width
        )
        return sqr_string


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))