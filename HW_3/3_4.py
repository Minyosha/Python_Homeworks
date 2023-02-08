# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number_to_convert = int(input('Введите натуральное положительное число для преобразования в двоичное:\n'))
list_1 = []

while number_to_convert > 0:
    if (number_to_convert % 2) == 0:
        list_1.insert(0, 0)
        number_to_convert = number_to_convert // 2
    else:
        list_1.insert(0, 1)
        number_to_convert = number_to_convert // 2

string = ''

for el in list_1:
    string += str(el)

print('Двоичное число:', string)


