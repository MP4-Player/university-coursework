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

class Vehicle(ABC):
    def __init__(self,price,speed, year):
        print("ввод общих данных")
        self.price = price
        self.speed = speed
        self. year =  year
        print(price,speed, year)
    
    @abstractmethod
    def set_coords(self):
        pass
    
    @abstractmethod 
    def get_coords(self):
        pass
    
    @abstractmethod
    def set_size(self):
        pass


    @staticmethod
    def Neuprice(price,price2):
        print("ввод скидки для машинны")
        return (price), (price-price*price2*0.05)
    
    @staticmethod
    def skrutka(speed,speed2):
        print("ввод скрученого пробега")
        return (speed-speed2+speed/speed2)
    
    @staticmethod
    def years(year):
        print("переиздать машину")
        if year<=1980:
            year=year+20
            print("новый год")
        else:
            year=year+5
            print("новейший год")
        return(year)
     

class Car(Vehicle):
    def __init__(self, price,speed, year,color):
        print("ввод данных машины")
        super().__init__(price,speed, year)
        self.color = color
    
    def get_coords(self):
        print("вввод данных машины")
        return self.price, self.speed, self.color
    
    def set_coords(self, pprice,yyear, sspeed, ccolor):
        print("новые данные машины")
        self.price = pprice
        self.speed = sspeed
        self. color = ccolor
        self. year = yyear


    def set_size(self):
        print("новые данные пробега")
        return self.speed+100
    
class Bicycle(Vehicle):
    def __init__(self, price,speed, year,color, hawy):
        print("ввод данных велика")
        super().__init__(price,speed,year)
        self.color = color
        self.hawy = hawy

    def get_coords(self):
        print("вывод данных велика")
        return self.price, self.speed, self.year, self.color,self.hawy
    
    def set_coords(self, price, speed, year, color,hawy):
       print("ввод данных велика")
       self.price = price
       self.speed = speed
       self. color =  color
       self.hawy = hawy
       self.year= year
       

class Lorry(Vehicle):
    def __init__(self, price,speed, year,kuzov):
        print("ввод данных Lorry")
        super().__init__(price,speed,year)
        self.kuzov = kuzov

    def get_coords(self):
        print("вывод данных Lorry")
        return self.price, self.speed, self.year, self.kuzov
    
    def set_coords(self, price, speed, kuzov):
       print("ввод данных kuzov")
       self.price = price
       self.speed = speed
       self. kuzov= kuzov


    def set_size(self):
        print("рекомендуемая цена")
        return self.speed**2 * self. year * (1/2)
    
    

class Garage:
    def __init__(self):
        self.Garage_list = []

    def add_Vehicle(self, transport):
        self.Garage_list.append(transport)

    def display_Vehicle(self):
        for transport in self.Garage_list:
            print("Сведения:", transport.get_coords())
            print("изменения:", transport.get_size())
            print()

#main
square = Car(1000000,90, 1890,"red")
square.set_coords(100,30, 100,"drank")
pyramid = Bicycle(40000,50, 2020,'blue', 3)
Lorryy=Lorry(40000,60,1896,1000)
figures = Garage()

figures.add_Vehicle(square)
figures.add_Vehicle(pyramid)
figures.add_Vehicle(Lorryy)

figures.display_Vehicle()

print(Vehicle.Neuprice(1000,30))
print(Vehicle.skrutka(90,100))
print(Vehicle.years(1700))