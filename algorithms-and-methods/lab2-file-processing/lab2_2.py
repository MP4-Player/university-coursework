import random
my_file = open("lab2_2.txt", "w+")

my_file.write("Hello, world!")

my_file.seek(0)

content = my_file.read()

char_to_insert = input("Введите символ: ")

insert_position = random.randint(0, len(content))

new_content = content[:insert_position] + char_to_insert + content[insert_position:]
my_file.seek(0)
my_file.write(new_content)


my_file.close()

print("Символ успешно вставлен в файл.")