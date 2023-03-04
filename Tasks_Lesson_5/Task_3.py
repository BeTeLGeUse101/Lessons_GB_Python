""" Создайте программу для игры в ""Крестики-нолики"". """

# Приветствие и инструкции
print("Добро пожаловать в игру Крестики-нолики!")
print("Чтобы сделать ход, введите номер ячейки от 1 до 9.")
print("Ячейки имеют следующие номера:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

# Создаем пустой список для игрового поля
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Функция для печати игрового поля
def print_board():
    for i in range(3):
        print(game_board[i*3] + "|" + game_board[i*3+1] + "|" + game_board[i*3+2])
        if i != 2:
            print("-----")

# Функция для проверки выигрыша
def check_win(player):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combination in winning_combinations:
        if game_board[combination[0]] == player and game_board[combination[1]] == player and game_board[combination[2]] == player:
            return True
    return False

# Основной цикл игры
current_player = "X"
while True:
    # Печатаем игровое поле и запрашиваем ход текущего игрока
    print_board()
    move = input(f"Ход игрока {current_player}: ")
    # Проверяем, что введено число от 1 до 9
    if move.isdigit() and int(move) >= 1 and int(move) <= 9:
        move = int(move) - 1  # преобразуем введенное число в индекс списка
        # Проверяем, что выбранная ячейка пуста
        if game_board[move] == " ":
            game_board[move] = current_player  # делаем ход
        else:
            print("Эта ячейка уже занята. Попробуйте снова.")
            continue  # переходим к следующей итерации цикла while
    else:
        print("Некорректный ввод. Введите число от 1 до 9.")
        continue

    # Проверяем, выиграл ли текущий игрок
    if check_win(current_player):
        print_board()
        print(f"Игрок {current_player} победил!")
        break  # завершаем игру

    # Проверяем, что на поле еще остались свободные ячейки
    if " " not in game_board:
        print_board()
        print("Ничья!")
        break  # завершаем игру

    # Передаем ход следующему игроку
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"