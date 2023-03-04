""" 
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

import random

def main():
    total_candies = 100
    player1_turn = random.choice([True, False]) # True - первый игрок начинает, False - второй игрок начинает

    # Пользователь выбирает режим игры: против бота или против другого игрока
    mode = int(input("Выберите режим игры: \n1. Игра против другого игрока\n2. Игра против бота\n"))

    if mode == 2:
        print("Вы выбрали игру против бота.")
        while total_candies > 0:
            print(f"Осталось конфет: {total_candies}")
            if player1_turn:
                candies_to_take = int(input("Вы, сколько конфет вы хотите взять (не более 28): "))
            else:
                candies_to_take = random.randint(1, min(total_candies, 28))
                print(f"Бот взял {candies_to_take} конфет.")
            while candies_to_take < 1 or candies_to_take > 28 or candies_to_take > total_candies:
                candies_to_take = int(input("Вы взяли неверное количество конфет. Введите число от 1 до 28, не больше, чем осталось конфет: "))
            total_candies -= candies_to_take
            player1_turn = not player1_turn

    else:
        print("Вы выбрали игру против другого игрока.")
        while total_candies > 0:
            print(f"Осталось конфет: {total_candies}")
            if player1_turn:
                candies_to_take = int(input("Первый игрок, сколько конфет вы хотите взять (не более 28): "))
            else:
                candies_to_take = int(input("Второй игрок, сколько конфет вы хотите взять (не более 28): "))
            while candies_to_take < 1 or candies_to_take > 28 or candies_to_take > total_candies:
                candies_to_take = int(input("Вы взяли неверное количество конфет. Введите число от 1 до 28, не больше, чем осталось конфет: "))
            total_candies -= candies_to_take
            player1_turn = not player1_turn

    if player1_turn:
        if mode == 2:
            print("Вы победили! Поздравляем!")
        else:
            print("Поздравляем! Первый игрок победил!")
    else:
        if mode == 2:
            print("Бот победил! Попробуйте еще раз!")
        else:
            print("Поздравляем! Второй игрок победил!")

main()