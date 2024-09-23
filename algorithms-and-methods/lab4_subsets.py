set_S = set("g fмиы о435 su")

set_A = set(filter(lambda x: x in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", set_S))
set_B = set(filter(lambda x: x in "abcdefghijklmnopqrstuvwxyz", set_S))
set_C = set(filter(lambda x: x.isdigit(), set_S))

print("Множество S:")
print(", ".join(set_S))

print("Подмножество А (русский алфавит):")
print(", ".join(set_A))

print("Подмножество Б (латинский алфавит):")
print(", ".join(set_B))

print("Подмножество В (цифры):")
print(", ".join(set_C))
