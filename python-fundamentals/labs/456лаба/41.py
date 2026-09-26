from abc import ABC, abstractmethod
from math import sqrt
class Point(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @abstractmethod
    def set_coords(self):
        pass
    
    @abstractmethod 
    def get_coords(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass

    @staticmethod
    def vector(x1 ,y1 ,x2 , y2):
        return (x2 - x1), (y2 - y1)
    
    @staticmethod
    def norma_v(x1 ,y1 ,x2 , y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    @staticmethod
    def norma_radius_v(x1 ,y1):
        return sqrt((x1**2 + y1**2))
     

class Square(Point):
    def __init__(self, x, y, side):
        super().__init__(x,y)
        self.side = side
    
    def get_coords(self):
        return self.x, self.y, self.side
    
    def set_coords(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side 

    def get_size(self):
        return self.side**2
    
class Pyramid(Point):
    def __init__(self, x, y, side, height):
        super().__init__(x,y)
        self.side = side
        self.height = height 

    def get_coords(self):
        return self.x, self.y, self.side, self.height
    
    def set_coords(self, x, y, side, height):
        self.x = x
        self.y = y
        self.side = side
        self.height = height

    def get_size(self):
        return self.side**2 * self.height * (1/3)
    

class Figures:
    def __init__(self):
        self.figures_list = []

    def add_figure(self, figure):
        self.figures_list.append(figure)

    def display_figures(self):
        for figure in self.figures_list:
            print("Coordinates:", figure.get_coords())
            print("Size:", figure.get_size())
            print()

#main
square = Square(1, 1, 5)
pyramid = Pyramid(2, 2, 6, 4)
figures = Figures()

figures.add_figure(square)
figures.add_figure(pyramid)

figures.display_figures()

print(Point.vector(1, 1, 2, 2))
print(Point.norma_v(0, 2, 3, 6))
print(Point.norma_radius_v(3,4))