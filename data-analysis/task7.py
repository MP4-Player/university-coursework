import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class House_prices():
    def __init__(self, dataframe_path, pallete="viridis"):
        self.df = pd.read_csv(dataframe_path)
        
        self.pallete = pallete
# 1 ЗАДАНИЕ
    def rename_columns(self, old2new):
        self.df.rename(columns=old2new, inplace=True)

    def replace_columns_values(self, column_name, old2new):

        self.df[column_name] = self.df[column_name].replace(old2new)

# 2 ЗАДАНИЕ
    def merge_columns(self, new_column_name, column_1, column_2):
        self.df[new_column_name] = self.df[column_1] - self.df[column_2]

# 3 ЗАДАНИЕ    
    def get_stats(self):
        numeric_cols = self.df.select_dtypes(include=[np.number])
        stats = numeric_cols.agg(['min', 'max', 'mean', 'median'])
        return stats
# 4 ЗАДАНИЕ
    def groupby(self, groupby_column, column):
        grouped = self.df.groupby(groupby_column)[column].mean().reset_index()
        grouped = grouped.sort_values(by='SalePrice', ascending=False)

        return grouped
    
    def get_histo(self, x, y, data):
        return sns.barplot(x=x, y=y, data=data, palette=self.pallete)

# 5 ЗАДАНИЕ   
    def filter_data(self, column, value_1, value_2):
        return self.df[(self.df[column] > value_1) & (self.df[column] < value_2)]
    
    def unique(self, column, filtered_data):
        unique_values = filtered_data[column].unique()
        duplicate_count = filtered_data.duplicated(subset=[column]).sum()
        return unique_values, duplicate_count
    
# 6 ЗАДАНИЕ
    def task_6(self, filtered_data):
        filtered_grouped = filtered_data.groupby('OverallQual')['SalePrice'].mean().reset_index()
        filtered_grouped = filtered_grouped.sort_values(by='SalePrice', ascending=False)

        return sns.barplot(x='OverallQual', y='SalePrice', data=filtered_grouped, palette=self.pallete)
    
# 7 ЗАДАНИЕ

    def task_7(self):
        numeric_cols = self.df.select_dtypes(include=[np.number])
        cross_tab = numeric_cols.agg(['min', 'max', 'mean', 'median']).transpose()

        print(cross_tab)

        # Построение 3D-гистограммы (требует библиотеки mpl_toolkits.mplot3d)
        from mpl_toolkits.mplot3d import Axes3D

        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Данные для графика
        _x = np.arange(len(cross_tab))
        _y = np.arange(4)
        _xx, _yy = np.meshgrid(_x, _y)
        x, y = _xx.ravel(), _yy.ravel()

        top = cross_tab.values.T.ravel()
        bottom = np.zeros_like(top)
        width = depth = 0.4

        ax.bar3d(x, y, bottom, width, depth, top, shade=True)

        ax.set_xticks(_x + width / 2)
        ax.set_xticklabels(cross_tab.index, rotation=90)
        ax.set_yticks(_y)
        ax.set_yticklabels(['min', 'max', 'mean', 'median'])
        ax.set_zlabel('Value')

        plt.show()

data = House_prices("train.csv")
#1
data.rename_columns({'LotArea': 'Lot_Size', 'YearBuilt': 'Year_Built'})
data.replace_columns_values("CentralAir", {'N': 'No', 'Y': 'Yes'})
#2
data.merge_columns("AgeDifference", "Year_Built", "YearRemodAdd")
#3
print(data.get_stats())
#4
groupby = data.groupby("OverallQual", "SalePrice")
histo = data.get_histo("OverallQual", "SalePrice", groupby)

filtered = data.filter_data("Lot_Size", 5000, 15000)
#5
print(data.unique("Lot_Size", filtered))

data.task_6(filtered)
data.task_7()
