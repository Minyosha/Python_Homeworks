# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Задайте число к для составления списка чисел Фиббоначи:\n'))
list_positive = [0, 1]
list_negative = [0, 1]

i = 1
while i < k:
    list_positive.append(list_positive[i] + list_positive[i - 1])
    list_negative.append(list_negative[i - 1] - list_negative[i])
    i = i + 1

list_negative_remastered = []

i = 0
while i < k:
    list_negative_remastered.insert(0, int(list_negative[i + 1]))
    i = i + 1

list_finished = list_negative_remastered + list_positive
print("Список чисел Фиббоначи для к =", k, ":")
print(list_finished)