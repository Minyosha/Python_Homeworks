# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

all_treats = 100
player_1_treats = 0
player_2_treats = 0
player_1_name = "Игрок 1"
player_2_name = "Игрок 2"
is_player_1_turn = True
is_bot = True

print("На столе", all_treats, "конфет. Играют два игрока делая ход друг после друга.")
print("Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.")
print("Все конфеты оппонента достаются сделавшему последний ход.")


def choose():
    bot_or_player = int(input('Для игры с человеком введите 1, для игры с компьютером введите 2:\n'))
    if bot_or_player == 2:
        global player_2_name
        player_2_name = "Компьютер"
    else:
        global is_bot
        is_bot = False


def roll():
    global is_player_1_turn
    coin = random.randint(0, 1)
    if coin == 1:
        print("Первый ход делает", player_1_name)
        is_player_1_turn = True
    else:
        print("Первый ход делает", player_2_name)
        is_player_1_turn = False


def turn():
    global is_player_1_turn
    global all_treats
    global is_bot
    if is_player_1_turn == True:
        player_1_turn()
    else:
        if is_bot == False:
            player_2_turn()
        else:
            bot_turn()


def player_1_turn():
    global is_player_1_turn
    global all_treats
    print("Ходит", player_1_name)
    while True:
        take_treats = int(input("Сколько конфет забрать? Введите количество от 1 до 28:\n"))
        if (take_treats <= all_treats) and (0 < take_treats < 29):
            all_treats = all_treats - take_treats
            print(player_1_name, "взял", take_treats, "конфет. На столе осталось:", all_treats, "конфет")
            is_player_1_turn = False
            return False
        else:
            print("Можно забирать от 1 до 28 конфет и не более", all_treats)


def player_2_turn():
    global is_player_1_turn
    global all_treats
    print("Ходит", player_2_name)
    while True:
        take_treats = int(input("Сколько конфет забрать? Введите количество от 1 до 28:\n"))
        if (take_treats <= all_treats) and (0 < take_treats < 29):
            all_treats = all_treats - take_treats
            print(player_2_name, "взял", take_treats, "конфет. На столе осталось:", all_treats, "конфет")
            is_player_1_turn = True
            return False
        else:
            print("Можно забирать от 1 до 28 конфет и не более", all_treats)


def bot_turn():
    global is_player_1_turn
    global all_treats
    print("Ходит", player_2_name)
    if (29 < all_treats < 57):
        take_treats = all_treats - 29
    elif (all_treats < 29):
        take_treats = all_treats
    else:
        take_treats = random.randint(1, 28)
    all_treats = all_treats - take_treats
    print(player_2_name, "взял", take_treats, "конфет. На столе осталось:", all_treats, "конфет")
    is_player_1_turn = True


choose()
roll()
while all_treats > 0:
    turn()

if is_player_1_turn == True:
    print("Победил", player_2_name)
else:
    print("Победил", player_1_name)
