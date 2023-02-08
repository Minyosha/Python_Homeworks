# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
number_input = (input('Введите вещественное число \n'))
number_without_minuses = number_input.replace('-', '')
number_without_dots = number_without_minuses.replace('.', '')
number_without_dots_and_commas = number_without_dots.replace('.', '')
summ_of_numbers = 0
for i in number_without_dots_and_commas:
        summ_of_numbers = summ_of_numbers + int(i)
print(summ_of_numbers)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number_n_input = int(input('Введите число N \n'))
print('Пусть N = ', number_n_input, ", тогда [ ", sep ="", end = "")
multiply_of_n = 1
for i in range(number_n_input):
    print(multiply_of_n * (i +1), end = "")
    multiply_of_n = multiply_of_n * (i +1)
    if (i+1) < number_n_input:
        print(", ", end = "")
print(" ] (", end = "")

for i in range(number_n_input):
    for x in range(i + 1):
        print((x +1), end = "")
        if (x+1) < (i + 1):
            print("*", end = "")
    if (i+1) < (number_n_input):
        print(", ", end = "")
print(")")


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input("Введите число n для последовательности (1+1/n)^n"))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.