# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
day = int(input('Введите день недели для проверки, является ли этот день выходным \n'))
if 0 < day < 6:
    print("Нет")
elif 5 < day < 8:
    print("Да")
else:
    print("Номер дня должен попадать в диапазон от 1 до 7")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            is_left = not (x or y or z)
            is_right = not x and not y and not z
            is_true = is_left == is_right
            print("Для A =", x, "B =", y, "C =", z, "выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно?", is_true)



 # Напишите программу, которая принимает на вход координаты точки (X и Y),
 # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
x_input = int(input('Введите координату X \n'))
y_input = int(input('Введите координату Y \n'))

if x_input > 0 and y_input > 0:
    print("Точка с координатами X =", x_input, " и Y =", y_input, " находится в 1 четверти")
elif x_input < 0 and y_input > 0:
    print("Точка с координатами X =", x_input, " и Y =", y_input, " находится в 2 четверти")
elif x_input < 0 and y_input < 0:
    print("Точка с координатами X =", x_input, " и Y =", y_input, " находится в 3 четверти")
elif x_input > 0 and y_input < 0:
    print("Точка с координатами X =", x_input, " и Y =", y_input, " находится в 4 четверти")
else:
    print("В введенных координатах не должно быть 0")


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
define_quarter = int(input('Введите номер четверти от 1 до 4 \n'))
if define_quarter == 1:
    print("В первой четверти x > 0, y > 0")
elif define_quarter == 2:
    print("Во второй четверти x < 0, y > 0")
elif define_quarter == 3:
    print("В третьей четверти x < 0, y < 0")
elif define_quarter == 4:
    print("В четвертой четверти x > 0, y < 0")
else:
    print("Номер четверти введет неверно")


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
x_input_a = float(input('Введите координату X точки A\n'))
y_input_a = float(input('Введите координату Y точки A \n'))
x_input_b = float(input('Введите координату X точки B\n'))
y_input_b = float(input('Введите координату Y точки B \n'))

distance = (((x_input_b - x_input_a)**2) + ((y_input_b - y_input_a)**2))**0.5

print("Расстояние между точкой А с координатами Xa =", x_input_a, "и Ya =", y_input_a, "и точкой B с координатами Xb =",
      x_input_b, "и Yb =", y_input_b, "равно", distance)

