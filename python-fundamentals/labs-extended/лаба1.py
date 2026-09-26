def number_of_lines(faile):
    N = 0
    with open(faile,'r') as f:
        for line in f:
            N += 1
        return N

file1 = "myFi.txt"
file2 = "myFile2.txt"
print("читаю:",file1)
print("читаю:",file2)

N1 = number_of_lines(file1)
N2 = number_of_lines(file2)

print("кол-во строк первого файла:",N1)
print("кол-во строк второго файла:",N2)

temp_file = "test50000.txt"
print("Кешфайл:",temp_file)

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(temp_file, 'w') as out_file:#открываем каждый файл для чтения а кеш файл для записи
    if N1 <= N2:
        for x, y in zip(f1, f2):#Python создает итератор, который объединяет элементы из нескольких источников данных, в случае тут с содержанием нужных нам файлов, а икс и игрик им тоже передаёться информация для хаписи формата зип(это делаеться для работы с циклами(к примру ещё и анзип))
            out_file.write("{0} - {1}".format(x.strip(), y))#Формат используеться для того чтобы передать данные(переменые ) в текст.Возврат по индексу ,возврата копии исходной строки путем удаления начальных и конечных пробелов, символов, переданных в функцию strip().
    else:
        for i in range(0,N2):#цикл работает о начала до конца второго файло(построчно)
            x = f1.readline()
            y = f2.readline()
            out_file.write("{0} -- {1}\n".format(x.strip(), y.strip()))#тут тоже самое
        for i in range(N2,N1):#возвращаем стёртые строки
            x = f1.readline()
            out_file.write(x)

with open(file1, 'w') as out_file, open(temp_file, 'r') as infile:#запись из кеш файла в наш файл
    for line in infile:
        out_file.write(line)