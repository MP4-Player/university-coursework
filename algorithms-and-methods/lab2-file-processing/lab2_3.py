def create_and_read_text_file(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if 1 <= n <= len(lines):
            print(f"Строка {n}: {lines[n-1]}")
        else:
            print(f"Строки с номером {n} не существует.")

filename = 'lab2_3.txt'

n = int(input("Введите строку:"))

create_and_read_text_file(filename, n)