# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Отрытие и создание файлов, необходимых для работы
file_1 = open('1 equation.txt', 'r')
file_2 = open('2 equation.txt', 'r')
file_result = open("equation result.txt", "w")

# Создание словарей
dictionary_1 = {}
dictionary_2 = {}
dictionary_result = {}
result_list = ()

# Извлечение коэффициентов и степеней многочлена из файла <1 equation.txt> и помещение их в словарь
print("Многочлен из файла <1 equation.txt>")
line_from_1 = file_1.readline()
print(line_from_1)
line_from_1 = line_from_1.replace('*x +', '*1 +')
line_from_1 = line_from_1.replace('*x = 0', '*x')
line_from_1 = line_from_1.replace(' ', '')
line_from_1 = line_from_1.replace('*x^', '*')
line_from_1 = line_from_1.replace('*x', '*1')
line_from_1 = line_from_1.replace('=', '*')
list_1 = line_from_1.split("+")

for i in list_1:
    coefficient, degree = i.split('*')
    dictionary_1.update({degree: coefficient})

print("Многочлен из файла <1 equation.txt> в представлении степень:коэффициент")
print(dictionary_1)

# Извлечение коэффициентов и степеней многочлена из файла <2 equation.txt> и помещение их в словарь
print("Многочлен из файла <2 equation.txt>")
line_from_2 = file_2.readline()
print(line_from_2)
line_from_2 = line_from_2.replace('*x +', '*1 +')
line_from_2 = line_from_2.replace('*x = 0', '*x')
line_from_2 = line_from_2.replace(' ', '')
line_from_2 = line_from_2.replace('*x^', '*')
line_from_2 = line_from_2.replace('*x', '*1')
line_from_2 = line_from_2.replace('=', '*')
list_2 = line_from_2.split("+")

for i in list_2:
    coefficient, degree = i.split('*')
    dictionary_2.update({degree: coefficient})

print("Многочлен из файла <2 equation.txt> в представлении степень:коэффициент")
print(dictionary_2)

# Объединение словарей, содержащих степени и коэффициенты многочленов 1 и 2 в единый список
result_list = (dictionary_1, dictionary_2)

# Суммирование коэффициентов многочленов для одинаковых значений степеней
for dictionary in result_list:
    for degree in dictionary:
        try:
            dictionary_result[degree] = int(dictionary_result[degree]) + int(dictionary[degree])
        except KeyError:
            dictionary_result[degree] = dictionary[degree]

# Сортировка по убыванию степени
sorted_list = sorted(dictionary_result.items(), reverse=True)

# Преобразование списка в словарь
dictionary_result = dict(sorted_list)

print("Финальный многочлен в представлении степень:коэффициент")
print(dictionary_result)

# Запись многочлена в файл <equation result.txt>
for degree, coefficient in dictionary_result.items():
    if int(degree) > 1:
        file_result.write(str(coefficient))
        file_result.write('*x^')
        file_result.write(str(degree))
        file_result.write(" + ")

    if int(degree) == 1:
        file_result.write(str(coefficient))
        file_result.write('*x')
        if str(0) in dictionary_result:
            file_result.write(" + ")

    if int(degree) == 0:
        file_result.write(str(coefficient))

file_result.write(" = 0")

# Завершение работы с файлами
file_result.close()
file_1.close()
file_2.close()

