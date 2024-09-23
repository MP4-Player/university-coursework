def set_input(set_name):
  print(f"Введите элементы множества {set_name} через пробел:")
  elements = input().split()
  return set(elements)

def printset(set_name, set_elements):
  print(f"Множество {set_name}:")
  print(", ".join(set_elements))
  print(f"Количество элементов: {len(set_elements)}")

# Задание множества A
set_A = set_input("A")
printset("A", set_A)

# Задание множества B
set_B = set_input("B")
printset("B", set_B)


