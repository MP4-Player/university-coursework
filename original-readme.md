from abc import ABC, abstractmethod
import math

class Body(ABC):
    @abstractmethod
    def surface_area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass

class Parallelepiped(Body):
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.depth + self.height * self.depth)
    
    def volume(self):
        return self.width * self.height * self.depth

class Cone(Body):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def surface_area(self):
        return math.pi * self.radius * (self.radius + math.sqrt(self.radius**2 + self.height**2))
    
    def volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height

class Ball(Body):
    def __init__(self, radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * math.pi * self.radius**2
    
    def volume(self):
        return (4/3) * math.pi * self.radius**3

class Series:
    def __init__(self):
        self.bodies = []
    
    def add_body(self, body):
        self.bodies.append(body)
    
    def list_bodies(self):
        for body in self.bodies:
            print(type(body).__name__)
            print("Площадь поверхности:", body.surface_area())
            print("Объем:", body.volume())
            print()

series = Series()

parallelepiped = Parallelepiped(2, 3, 4)
cone = Cone(5, 6)
ball = Ball(7)


series.add_body(parallelepiped)

series.add_body(cone)

series.add_body(ball)

series.list_bodies()

