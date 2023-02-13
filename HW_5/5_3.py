# Создайте программу для игры в ""Крестики-нолики""

global is_win
is_win = False


field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_map():
    print(field[0], field[1], field[2])
    print(field[3], field[4], field[5])
    print(field[6], field[7], field[8])


def player_1_turn():
    global is_player_1_turn
    while True:
        coordinate = int(input("Введите номер клетки, чтобы поставить X:\n"))
        coordinate = coordinate - 1
        if (0 <= coordinate < 9) and (field[coordinate] != "X") and (field[coordinate] != "0"):
            field[coordinate] = "X"
            is_player_1_turn = False
            return False
        else:
            print("Номер клетки должен быть от 1 до 9 и клетка не должна быть занята")


def player_2_turn():
    global is_player_1_turn
    while True:
        coordinate = int(input("Введите номер клетки, чтобы поставить 0:\n"))
        coordinate = coordinate - 1
        if (0 <= coordinate < 9) and (field[coordinate] != "X") and (field[coordinate] != "0"):
            field[coordinate] = "0"
            is_player_1_turn = False
            return False
        else:
            print("Номер клетки должен быть от 1 до 9 и клетка не должна быть занята")


def check_for_win():
    win = ""
    global is_win
    for i in victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
            print("Победил", win)
            is_win = True
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"
            print("Победил", win)
            is_win = True

    return win


print_map()
while is_win is False:
    player_1_turn()
    win = check_for_win()
    if is_win is True:
        break
    print_map()
    player_2_turn()
    win = check_for_win()
    print_map()