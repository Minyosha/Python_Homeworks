# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = float(input('Введите точность вычисления числа Pi в формате 0.001:\n'))

pi = float(0)
iteration = float(d + 1)
n = int(0)
rounding_number = int(0)
accuracy_counter = d

while accuracy_counter < 1:
    accuracy_counter = accuracy_counter * 10
    rounding_number = rounding_number + 1

while abs(iteration) > d:
    iteration = 4 * (((-1)**n)/((2 * n) + 1))
    pi = pi + iteration
    n = n + 1

print('Точность вычисления числа Pi:', rounding_number, "знаков после запятой. Число Pi:", round(pi, rounding_number))