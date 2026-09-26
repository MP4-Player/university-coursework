import numpy

def first():
    try:
        print("Найти индексы ненулевых элементов в заданном массиве.")
        text=(input("Введите элементы массива: ").split())
        text_k=[int(x) for x in  text]
        text_l=numpy.flatnonzero(text_k)
        print("индексы:", text_l)
    
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.") 

def second():
     try:
         a=int(input("Введите длину марицы"))
         b=int(input("Введите высоту марицы"))
         s = (a,b)
         d=numpy.ones(s)
         print(d)
     except ValueError:print("Неправильный ввод. Попробуйте еще раз.") 

def third():
    try:
        a=int(input("Введите нижний порог рандома"))
        b=int(input("Введите верхний порог рандома"))
        s = int(input("Введите высоту матрицы"))
        rand_int2 = numpy.random.randint(a,b,(s,3))
        print("Тадам!", rand_int2)
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")
 
            
#first second third fourth fifth sixth seventh eighth ninth tenth


a=input("0-Выход, 1-Найти индексы ненулевых элементов в заданном массиве, 2-Создать nxn единичную матрицу., 3-Создать массив nxnxn со случайными значениями ")
while a!="0":
    if a=="1":
        first()
    elif a=="2":
        second()
    elif a=="3":
        third()
        #re.sub(r'[0-9]',text)
    else:
        print("Неверный ввод!")
    a=input("0-Выход, 1-Найти индексы ненулевых элементов в заданном массиве, 2-Создать nxn единичную матрицу., 3-Создать массив nxnxn со случайными значениями")
