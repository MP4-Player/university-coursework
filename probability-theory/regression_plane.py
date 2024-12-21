import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress


file_path = '5.xlsx' 
data = pd.read_excel(file_path, skiprows=2) 


data.columns = ['ID', 'Пол', 'Вариант', '1_общ', '1_замена', '1_по_час', '1_рац', '1_триг', '1_иррац', '1_доп', 'Результат1',
                '2_вариант', '2_текст', '2_параметр', '2_поляр', '2_вращ', '2_дуга', '2_несоб', '2_доп', 'Результат2',
                '3_с_разд', '3_однород', '3_лин', '3_Бернулли', '3_доп', 'Результат3']

# Извлечение столбцов с результатами контрольных работ
X = data['Результат1'].values.reshape(-1, 1)  
Y = data['Результат2'].values.reshape(-1, 1)  
Z = data['Результат3'].values 

# Удаляем строки, где Z отсутствует (если третья контрольная не заполнена)
data_filtered = data.dropna(subset=['Результат3'])
X_filtered = data_filtered['Результат1'].values.reshape(-1, 1)
Y_filtered = data_filtered['Результат2'].values.reshape(-1, 1)
Z_filtered = data_filtered['Результат3'].values

# Объединяем X и Y в одну матрицу признаков
XY = np.hstack([X_filtered, Y_filtered])

# Создаем модель линейной регрессии для Z = aX + bY + c
model_z = LinearRegression()
model_z.fit(XY, Z_filtered)

# Получаем коэффициенты регрессии для Z
a, b = model_z.coef_  # Коэффициенты для X и Y
c = model_z.intercept_  # Свободный член

# Уравнение плоскости регрессии: Z = a*X + b*Y + c
print(f"Уравнение плоскости регрессии: Z = {a:.2f}*X + {b:.2f}*Y + {c:.2f}")

# Линейная регрессия между Y и X
slope_yx, intercept_yx, _, _, _ = linregress(X_filtered.flatten(), Y_filtered.flatten())

# Линейная регрессия между Z и X
slope_zx, intercept_zx, _, _, _ = linregress(X_filtered.flatten(), Z_filtered.flatten())

# Линейная регрессия между Y и Z
slope_yz, intercept_yz, _, _, _ = linregress(Y_filtered.flatten(), Z_filtered.flatten())

# Уравнения линий регрессии
print(f"Уравнение линии регрессии между Y и X: Y = {slope_yx:.2f}*X + {intercept_yx:.2f}")
print(f"Уравнение линии регрессии между Z и X: Z = {slope_zx:.2f}*X + {intercept_zx:.2f}")
print(f"Уравнение линии регрессии между Y и Z: Z = {slope_yz:.2f}*Y + {intercept_yz:.2f}")

# Построение 3D графика с точками
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Точки (X, Y, Z)
ax.scatter(X_filtered, Y_filtered, Z_filtered, c='blue', marker='o', label='Точки (X, Y, Z)')

# Построение плоскости регрессии
x_plane = np.linspace(0, 1, 100)
y_plane = np.linspace(0, 1, 100)
x_plane, y_plane = np.meshgrid(x_plane, y_plane)
z_plane = a * x_plane + b * y_plane + c

# Отображение плоскости
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5, color='red', label='Плоскость регрессии (XYZ)')

# Построение линии регрессии между Y и X
x_line = np.linspace(0, 1, 100)
y_line = slope_yx * x_line + intercept_yx
z_line = np.full_like(x_line, np.mean(Z_filtered))  # Линия на среднем значении Z
ax.plot(x_line, y_line, z_line, c='green', label='Линия регрессии между Y и X')

# Построение линии регрессии между Z и X
z_line_zx = slope_zx * x_line + intercept_zx
y_line_zx = np.full_like(x_line, np.mean(Y_filtered))  # Линия на среднем значении Y
ax.plot(x_line, y_line_zx, z_line_zx, c='purple', label='Линия регрессии между Z и X')

# Построение линии регрессии между Y и Z
z_line_yz = slope_yz * y_line + intercept_yz
x_line_yz = np.full_like(y_line, np.mean(X_filtered))  # Линия на среднем значении X
ax.plot(x_line_yz, y_line, z_line_yz, c='orange', label='Линия регрессии между Y и Z')

# Настройка графика
ax.set_xlabel('X (Результат первой контрольной)')
ax.set_ylabel('Y (Результат второй контрольной)')
ax.set_zlabel('Z (Результат третьей контрольной)')
ax.set_title('Трёхмерный закон распределения и регрессии')
ax.legend()

plt.ion()  
plt.show(block=True)

plt.ioff() 