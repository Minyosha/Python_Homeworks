# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N:\n'))

list_1 = []
simple_divider = 2
number_for_dividing = n

while simple_divider <= number_for_dividing:
    if number_for_dividing % simple_divider == 0:
        list_1.append(simple_divider)
        number_for_dividing //= simple_divider
        simple_divider = 2
    else:
        simple_divider = simple_divider + 1

print("Список простых множителей числа N =", n, ":", list_1)