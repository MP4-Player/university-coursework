import random

my_file = open("lab2_1.txt", "w+")
count = int(input("Введите кол-во элементов: "))

for x in range(count):
    my_file.write(str(random.randint(-100,100)))
    my_file.write(" ")
my_file.close()


my_file = open("lab2_1.txt", "r")
content = my_file.read()

count_negative = 0
numbers = content.split()

for i in numbers:
    if int(i) < 0:
        count_negative += 1 

print('количество отрицательных элементов:',count_negative)
        
my_file.close()