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
        s = int(input("Введите высоту матрицы(желательно 3 ибо это условие)"))
        rand_int2 = numpy.random.randint(a,b,(s,3))
        print("Тадам!", rand_int2)
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")


def fourth():
    try:
        a=int(input("Введите нижний порог рандома"))
        b=int(input("Введите верхний порог рандома"))
        n = numpy.random.randint(a, b)
        print(n)
        vector = numpy.zeros((n), dtype='int64')
        print(vector)
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")


def fifth ():
    try:
        a=int(input("Введите нижний порог рандома"))
        b=int(input("Введите верхний порог рандома"))
        n = numpy.random.randint(a, b)
        print(n)
        vector = numpy.zeros((1,n), dtype='int64')
        vector[0,4] = 1
        print(vector)

    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")


def sixth ():
    try:
        a=int(input("Введите нижний порог "))
        b=int(input("Введите верхний порог"))
        vector = numpy.arange(a,b+1,dtype='int64')
        print(vector)
        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")


def seventh ():
    try:
        b=int(input("Введите верхний порог рандома"))
        a=int(input("Введите длинну"))
        arr = numpy.random.randint(b,size=a)
        print(arr)
        arr = numpy.flip(arr)
        print(arr)  
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")



def eighth ():
    try:
        n = numpy.random.randint(2,10+1)
        m = numpy.random.randint(2,10+1)
        print(n,m)
        matrix = numpy.ones((n,m),dtype='int64')
        if (n != 2) and (m != 2):
            matrix[1:-1, 1:-1] = 0
            print(matrix)
        else:
            print(matrix)
            print()
        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")



def ninth ():
    try:
        b=int(input("Введите верхний порог"))
        n = numpy.random.randint(2,b+1)
        print(n)
        matrix = numpy.arange(1,n+1,dtype='int64')  * numpy.eye(n,k=-1,dtype='int64') 
        print(matrix)
        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")




def tenth():
    try:
        b=int(input("Введите верхний порог рандома"))
        n = numpy.random.randint(2, b+1)
        print(n)
        matrix = numpy.zeros((n,n), dtype='int64')
        matrix[::2,::2] = 1
        matrix[1::2,1::2] = 1
        print(matrix)
        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")



def eleventh ():
    try:
        b=int(input("Введите верхний порог рандома"))
        arr = numpy.random.randint(-10,10+1,size= numpy.random.randint(2,b+1))
        print(arr)
        index_max = numpy.argwhere(arr == numpy.amax(arr))
        print(index_max)
        arr[index_max]=0
        print(arr)

        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")




def twelfth ():
    try:
        value = numpy.random.randint(-10,10+1)
        print(value)
        arr = numpy.random.randint(-10,10+1,size= numpy.random.randint(2,10+1))
        print(arr)
        index_abs = numpy.abs(arr - value)
        #print(index_abs)
        index_min = numpy.argwhere(index_abs == numpy.amin(index_abs))
        print("ближайшее число это",index_min+1,"е")

        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")




def thirteenth ():
    try:
        arr = numpy.random.randint(0, 10, size=(2, 3, 4, 5))
        print(arr)
        result = numpy.sum(arr,axis=(-2,-1))
        print(result)


        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")



def  fourteenth():
    try:
        arr = numpy.array([[1, 0, 3],[4, 0, 6],[7, 0, 9]])
        result = numpy.all(arr == 0, axis=0)
        print(result)


        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")



def fifteenth():
    try:
        n = numpy.random.randint(2,5+1)
        m = numpy.random.randint(2,5+1)
        print(n,m)
        matrix = numpy.random.randint(0, 10, size=(n,m))
        print(matrix)
        result = numpy.mean(matrix, axis=1, keepdims=True)
        print(result)
        print(matrix - result)
        
    except ValueError:print("Неправильный ввод. Попробуйте еще раз.")




 
            
#first second third fourth fifth sixth seventh eighth ninth tenth


a=input("0-Выход, 1-Найти индексы ненулевых элементов в заданном массиве, 2-Создать nxn единичную матрицу., 3-Создать массив nxnxn со случайными значениями 4. Создать вектор (одномерный массив) размера n, заполненный нулями5. Создать вектор размера 1n, заполненный нулями, но пятый элемент равен 1 6. Создать вектор со значениями от n до m 7. Развернуть одномерный массив (первый становится последним) 8. Создать матрицу с 0 внутри, и 1 на границах 9. Создать nxn матрицу с 1,2,..,n-1 под диагональю 10.Создать nxn матрицу и заполнить её в шахматном порядке 11.Заменить максимальный элемент на ноль 12.Найти ближайшее к заданному значению число в заданном массиве 13.Дан четырехмерный массив, посчитать сумму по последним двум осям 14.Определить, есть ли в 2D массиве нулевые столбцы  15.Отнять среднее из каждой строки в матрице")
while a!="0":
    if a=="1":
        first()
    elif a=="2":
        second()
    elif a=="3":
        third()
    elif a=="4":
        fourth()
    elif a=="5":
        fifth ()
    elif a=="6":
        sixth()
    elif a=="7":
        seventh ()
    elif a=="8":
        eighth()
    elif a=="9":
        ninth ()
    elif a=="10":
        tenth()
    elif a=="11":
        eleventh()
    elif a=="12":
        twelfth ()
    elif a=="13":
        thirteenth()
    elif a=="14":
         fourteenth()
    elif a=="15":
        fifteenth()
        #re.sub(r'[0-9]',text)
    else:
        print("Неверный ввод!")
    a=input("0-Выход, 1-Найти индексы ненулевых элементов в заданном массиве, 2-Создать nxn единичную матрицу., 3-Создать массив nxnxn со случайными значениями 4. Создать вектор (одномерный массив) размера n, заполненный нулями5. Создать вектор размера 1n, заполненный нулями, но пятый элемент равен 1 6. Создать вектор со значениями от n до m 7. Развернуть одномерный массив (первый становится последним) 8. Создать матрицу с 0 внутри, и 1 на границах 9. Создать nxn матрицу с 1,2,..,n-1 под диагональю 10.Создать nxn матрицу и заполнить её в шахматном порядке 11.Заменить максимальный элемент на ноль 12.Найти ближайшее к заданному значению число в заданном массиве 13.Дан четырехмерный массив, посчитать сумму по последним двум осям 14.Определить, есть ли в 2D массиве нулевые столбцы  15.Отнять среднее из каждой строки в матрице")