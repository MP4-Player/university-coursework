import matplotlib.pyplot as plt
import numpy as np

class Grafic:
    def __init__(self, n, m, k):
        self.x=np.linspace(n, m, k)
        self.y=np.linspace(n, m, k)

    def Z1(self):
        
        mu = 7
        sigma = 4
        plt.title("Задание №1")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(which='both')
        y1 = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-np.square(self.x - mu)/np.square(sigma))
        y2 = (1/((sigma+1)*np.sqrt(2*np.pi)))*np.exp(-np.square(self.x - (mu+1))/np.square(sigma+1))
        plt.plot(self.x, y1, label="y1")
        plt.plot(self.x, y2, "r--", label="y2")
        plt.legend()
        plt.show()

    def Z2(self):

        plt.title("Задание №2")
        for i in range(10):
            white_noise = np.random.uniform(-1, 1, size=len(self.x))
            plt.plot(self.x, white_noise, label=f'График {i+1}')
        plt.xlabel('Аргумент')
        plt.ylabel('Значение')
        plt.legend()
        plt.show()

    
    def Z3(self):
 
        activities = ['Сон', 'Учеба в вузе', 'Обед', 'Учеба дома', 'уборка', 'Отдых','     залипание в телефоне']
        time_spent = [3, 8, 1, 4, 1, 3,4]
        plt.figure(figsize=(10, 7))
        plt.bar(activities, time_spent, color='red')
        plt.xlabel('Виды занятий')
        plt.ylabel('Время')
        plt.title('Распределение времени на занятия в течение дня')
        plt.show()

    def Z4(self):
        X, Y = np.meshgrid(self.x, self.y)
        Z = X**2 - 3*X*Y + Y**2 + X + 2*Y + 5
        plt.contour(X, Y, Z, levels=[0], colors='r')
        plt.title('График неявной функции x^2 - 3xy + y^2 + x + 2y + 5 = 0')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.show()

    def Z5(self):
    
        x, y = np.meshgrid(self.x, self.y)

        z = (((x-5+(((x-5)**2)+2**2)**0.5)*(7-x+(((7-x)**2)+2**2)**0.5))/(4*((((x-5)**2)+2**2)**0.5)*((((7-x)**2)+2**2)**0.5)))*(((y-3+(((y-3)**2)+2**2)**0.5)*(10-y+(((10-y)**2)+2**2)**0.5))/(4*((((y-3)**2)+2**2)**0.5)*((((10-y)**2)+2**2)**0.5)))

        # Строим график
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')
        ax.plot_surface(x, y, z)

        # Настройка меток
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Показываем график
        plt.show()


n=int(input('Введите значение от: '))
m=int(input('Введите значение до: '))
k=int(input('Введите количество точек разбиения: '))
test=Grafic(n, m, k)
test.Z1()
test.Z2()
test.Z3()
test.Z4()
test.Z5()
