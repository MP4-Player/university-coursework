"""
Создать абстрактный класс Vehicle. На его основе реализовать классы
Car (автомобиль), Bicycle (велосипед) и Lorry (грузовик). Классы
должны иметь возможность задавать и получать параметры средств
передвижения (цена, максимальная скорость, год выпуска и т. д.).
Наряду с общими полями и методами, каждый класс должен
содержать и специфичные для него поля.
*Создать класс Garage, содержащий массив/параметризованную
коллекцию объектов этих классов в динамической памяти.
Предусмотреть возможность вывода характеристик объектов списка.
Написать демонстрационную программу, в которой будут
использоваться все методы классов.
"""
from abc import ABC, abstractmethod
from math import sqrt
class Vehicle(ABC):
    def __init__(self,price,speed, year):
        self.price = price
        self.speed = speed
        self. year =  year
    
    @abstractmethod
    def set_price(self):
        pass
    
    @abstractmethod 
    def get_price(self):
        pass
    
    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod 
    def get_speed(self):
        pass

    @staticmethod
    def Neuprice(price,price2):
        return (price), (price-price*price2)
    
    @staticmethod
    def skrutka(speed,speed2):
        return (speed-speed2+speed/speed2)
    
    @staticmethod
    def years(year):
        if year<=1980:
            year+20
        else:
            year+5
        return(year)
     

class Car(Vehicle):
    def __init__(self, price,speed, year,color):
        super().__init__(price,speed, year)
        self.color = color
    
    def get_coords(self):
        return self.price, self.speed, self.color
    
    def set_coords(self, x, y, side):
        self.price = price
        self.speed = speed
        self. color =  color
    
class Bicycle(Vehicle):
    def __init__(self, price,speed, year,color, hawy):
        super().__init__(price,speed,year)
        self.color = color
        self.hawy = hawy

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

print(Vehicle.vector(1, 1, 2, 2))
print(Vehicle.norma_v(0, 2, 3, 6))
print(Vehicle.norma_radius_v(3,4))