# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_1 = input("Введите список чисел, разделенных пробелом: ").split()

print(list_1)

list_1 = list(set(list_1))

print("Удаление повторяющихся чисел из списка")

print(list_1)