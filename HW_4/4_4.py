# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

file = open("equation.txt", "w")

k = int(input('Введите степень k для генерации многочлена:\n'))

current_degree = k

list_1 = []

while current_degree > 0:
    constant_for_x = random.randint(0, 100)
    list_1.append(constant_for_x)
    if constant_for_x != 0:
        file.write(str(constant_for_x))
        if current_degree > 1:
            file.write("*x^")
            file.write(str(current_degree))
        elif current_degree == 1:
            file.write("*x")
        current_degree = current_degree - 1
    else:
        current_degree = current_degree - 1

    if (constant_for_x != 0) and current_degree > 0:
        file.write(" + ")

constant = random.randint(0, 100)

if constant != 0:
    file.write(" + ")
    file.write(str(constant))
    file.write(" = 0")
else:
    file.write(" = 0")

print("Многочлен со старшей степенью", k, "сгенерирован в файл equation.txt")
print("Список коэффициентов многочлена со старшей степенью", k, "по убыванию степеней для x:")
print(list_1)

file.write("\n")
file.write("Список коэффициентов многочлена со старшей степенью ")
file.write(str(k))
file.write(" по убыванию степеней для x:")
file.write("\n")
file.write(str(list_1))

file.close()