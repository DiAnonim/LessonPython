
# Вам предстоит создать простую текстовую игру в крестики-нолики на Python. Игра
# должна уметь выполнять следующие задачи:

# 1. Отображение игрового поля: Игровое поле представляет собой сетку 3x3. Вы можете
# использовать двухмерный список для представления поля. Каждая ячейка на поле может быть
# либо "X", либо "O", либо " " (пустой).

# 2. Ввод игроков: Игра играется двумя игроками. Игрок 1 использует "X", а игрок 2
# использует "O". Игроки по очереди ставят свой знак в пустую ячейку. Игрок должен ввести
# номер строки и столбца (1-3), чтобы поставить свой знак.

# 3. Проверка на победу: После каждого хода игры должна проверять, выиграл ли текущий
# игрок. Игрок выигрывает, если у него есть 3 своих знака в ряду, столбце или диагонали.

# 4. Проверка на ничью: Если поле заполнено, и ни один игрок не выиграл, игра
# заканчивается вничью.

# 5. Цикл игры: Игра должна продолжаться, пока один из игроков не выиграет или игра
# не закончится вничью. После окончания игры игроков должны спросить, хотят ли они сыграть
# еще раз.

# Подсказка: Вы можете использовать цикл while для цикла игры и вложенные циклы for
# для отображения игрового поля и проверки на победу. Вы можете использовать операторы ifelif для обработки ввода игрока и проверки на победу или ничью.

# Бонус: Для дополнительной практики на Python добавьте функцию в свою программу,
# которая позволяет игрокам выбирать свой собственный знак вместо "X" и "O". Знаки должны
# быть одними символами.




def print_board():
    for row in gameMap:
        print(" ".join(row))
    print()

def check_winner():
    for i in range(3):
        if gameMap[i][0] == gameMap[i][1] == gameMap[i][2] != "-":
            return True
        if gameMap[0][i] == gameMap[1][i] == gameMap[2][i] != "-":
            return True

    if gameMap[0][0] == gameMap[1][1] == gameMap[2][2] != "-":
        return True
    if gameMap[0][2] == gameMap[1][1] == gameMap[2][0] != "-":
        return True

    return False

def check_draw():
    for row in gameMap:
        if "-" in row:
            return False
    return True

def choose_sign(player):
    sign = input(f"Player {player}, choose your sign (one character): ")
    return sign

gameMap = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

playerOne = choose_sign(1)
playerTwo = choose_sign(2)

isPlayerOne = True
isWin = False

while not isWin and not check_draw():
    print_board()

    if isPlayerOne:
        print("Player One")
        sign = playerOne
    else:
        print("Player Two")
        sign = playerTwo

    coord = input("Enter row and column (number number): ").split(" ")

    row = int(coord[0]) - 1
    col = int(coord[1]) - 1

    if 0 <= row < 3 and 0 <= col < 3 and gameMap[row][col] == "-":
        gameMap[row][col] = sign
        isWin = check_winner()
        isPlayerOne = not isPlayerOne
    else:
        print("Invalid move. Try again.")

print_board()

if isWin:
    print(f"Player {'One' if not isPlayerOne else 'Two'} wins!")
else:
    print("It's a draw!")


