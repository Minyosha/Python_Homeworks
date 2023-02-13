import math

'''m = 750
n = 700
print(math.ceil(m/n))



class1 = int(input('Введите количество учеников в 1 классе \n'))
tables1 = math.ceil(class1/2)
class2 = int(input('Введите количество учеников во 2 классе \n'))
tables2 = math.ceil(class2/2)
class3 = int(input('Введите количество учеников в 3 классе \n'))
tables3 = math.ceil(class3/2)
print('Необходимое количество парт:')
print(tables1+tables2+tables3)


vagonNumberHead = int(input('Введите номер вагона с головы поезда \n'))
vagonNumberTail = int(input('Введите номер вагона с конца поезда \n'))
print(vagonNumberTail+vagonNumberHead-1)


year = int(input('Введите год \n'))
if year % 400 == 0:
    print("Год високосный")
elif year % 100 == 0:
    print("Год не високосный")
elif year % 4 == 0:
    print("Год високосный")
else:
    print("Год не високосный")

'''
my_list = [2, 5, 9, 1, 2]

for i in range(len(my_list)):
    if i % 2 == 0:
        my_list[i] *= -1

print(my_list)




def check(symbol):
    global i
    global j
    for i in range(len(field)):
        for j in range(len(field[i])):
            if ((field[0][0] and field[1][1] and field[2][2]) == symbol) or \
                    ((field[2][0] and field[1][1] and field[0][2]) == symbol) or \
                    ((field[i][0] and field[i][1] and field[i][2]) == symbol) or \
                    ((field[0][j] and field[1][j] and field[2][j]) == symbol):
                print(symbol, "победил")
                global is_win
                is_win = True


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# ручной режим
def input_numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = input_numbers(3)

if check_predicate(statement):
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")