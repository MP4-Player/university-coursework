import pandas as pd
import random 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Baze:
    def __init__(self,file):
        self.file=pd.read_csv(file, delimiter=",")
        self.file.columns=["Index","Number", "Count", "Population", "Non"]
        

    def Info(self):
        print(self.file[:5])       

    def New_Name(self, start_title, new_title):
        print(self.file.columns)
        self.file.rename(columns={start_title: new_title}, inplace=True)
        print(self.file.columns)
        self.file.to_csv("POP1.csv")
        

    def New_value(self):
        self.file["Unknow"]=self.file["Unknow"].fillna(random.randint(0,10))
        self.Info()
          

    def New_column(self):
        self.file["New_column"]=self.file['Number'].astype(str)#+self.file["Unknow"].astype(str)
        print(self.file[:5])

    def Mathem(self):
        self.file["Number"] = self.file["Number"].astype(int)
        print(self.file["Number"].agg(['min', 'max', 'mean', 'median']))
        self.file["Population"] = self.file["Population"].astype(int)
        print(self.file["Population"].agg(['min', 'max', 'mean', 'median']))



    def Group(self):
        print("Сортировка по убыванию")
        a=self.file.groupby(["User Rating"], sort=True).agg({'User Rating': ["mean"]}).reset_index()
        print(a)
        a.plot(kind="bar")

    def filtr(self):
        self.file[self.file["Runtime"].isnull() == True] = "0 min"
        self.file["Runtime"] = self.file["Runtime"].apply(lambda x: x.replace("min", "").replace(" ", "").replace(",", ""))
        self.file["Runtime"].unique()
        self.file["Runtime"] = self.file["Runtime"].astype(int)
        self.file["Runtime"].info()
        sorted = self.file[(self.file["Runtime"] > 13) & (self.file["Runtime"] < 28)]
        print("Уникальные значения: ")
        print(sorted["Runtime"].unique())
        print("Количество дубликатов: ")
        print(sorted["Runtime"].value_counts())

    def Graf(self):
        sorted["Runtime"].value_counts().plot.bar()

    def Svod_table(self):
        # Выберем только числовые столбцы для анализа
        numeric_columns = ['User Rating', 'Number of Votes', 'Runtime', 'Metascore', 'Gross']
        for col in numeric_columns:
            sorted[col] = sorted[col].astype(str)
            sorted[col] = sorted[col].apply(lambda x: x.replace(",", "").replace(" ", "").replace("nan", "0"))
            sorted[col] = sorted[col].astype(float)
        # Создадим перекрестную выборку с агрегированными значениями
        cross_data = sorted[numeric_columns].agg(['min', 'max', 'mean', 'median'])
        # Выведем перекрестную выборку
        print(cross_data)

dt=Baze(r"C:\Users\Пользователь\Desktop\програмироание\1и2лаба\POP.csv")
#Задание 1
dt.Info()
#Смена названия столбцов
dt.New_Name("Count","Strana")
dt.New_Name("Non","Unknow")

#Новые значения
#dt.New_value()

#Новый столбец
dt.New_column()

#Данные по числовым столбцам
dt.Mathem()