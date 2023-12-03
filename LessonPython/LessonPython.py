
# ��� ��������� ������� ������� ��������� ���� � ��������-������ �� Python. ����
# ������ ����� ��������� ��������� ������:

# 1. ����������� �������� ����: ������� ���� ������������ ����� ����� 3x3. �� ������
# ������������ ���������� ������ ��� ������������� ����. ������ ������ �� ���� ����� ����
# ���� "X", ���� "O", ���� " " (������).

# 2. ���� �������: ���� �������� ����� ��������. ����� 1 ���������� "X", � ����� 2
# ���������� "O". ������ �� ������� ������ ���� ���� � ������ ������. ����� ������ ������
# ����� ������ � ������� (1-3), ����� ��������� ���� ����.

# 3. �������� �� ������: ����� ������� ���� ���� ������ ���������, ������� �� �������
# �����. ����� ����������, ���� � ���� ���� 3 ����� ����� � ����, ������� ��� ���������.

# 4. �������� �� �����: ���� ���� ���������, � �� ���� ����� �� �������, ����
# ������������� ������.

# 5. ���� ����: ���� ������ ������������, ���� ���� �� ������� �� �������� ��� ����
# �� ���������� ������. ����� ��������� ���� ������� ������ ��������, ����� �� ��� �������
# ��� ���.

# ���������: �� ������ ������������ ���� while ��� ����� ���� � ��������� ����� for
# ��� ����������� �������� ���� � �������� �� ������. �� ������ ������������ ��������� ifelif ��� ��������� ����� ������ � �������� �� ������ ��� �����.

# �����: ��� �������������� �������� �� Python �������� ������� � ���� ���������,
# ������� ��������� ������� �������� ���� ����������� ���� ������ "X" � "O". ����� ������
# ���� ������ ���������.




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


