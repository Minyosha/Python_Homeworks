# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_1 = [2, 3, 5, 9, 3]
summa = 0
pos_number = 0
for i in list_1:
    if ((pos_number % 2) != 0):
        summa = summa + i
    pos_number = pos_number + 1
print('Сумма элементов списка', list_1, ', стоящих на нечетной позиции: ', summa, end = "")