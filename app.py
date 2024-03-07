board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # закидываем доску для игры в двумерный массив

def draw_board():  # рисуем доску
    print(board[0][0], board[0][1], board[0][2]), print(board[1][0], board[1][1], board[1][2]), print(
        board[2][0], board[2][1], board[2][2])


def attempt_generationx():  # игрок 1 делает ход крестиком
    print('Введите номер клетки, на которую хотите поставить крестик')
    attempt = int(input())
    if attempt in [1, 2, 3]:
        board[0][attempt - 1] = 'X'
    if attempt in [4, 5, 6]:
        board[1][attempt - 4] = 'X'
    if attempt in [7, 8, 9]:
        board[2][attempt - 7] = 'X'
    draw_board()


def attempt_generation0():  # игрок 2 делает ход ноликом
    print('Введите номер клетки, на которую хотите поставить нолик')
    attempt = int(input())
    if attempt in [1, 2, 3]:
        board[0][attempt - 1] = 'O'
    if attempt in [4, 5, 6]:
        board[1][attempt - 4] = 'O'
    if attempt in [7, 8, 9]:
        board[2][attempt - 7] = 'O'
    draw_board()


def check_draw():  # делаем проверку на ничью
    if not ((board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2]) or (
            board[2][0] == board[2][1] == board[2][2]) or (board[0][0] == board[1][0] == board[2][0]) or (
                    board[0][1] == board[1][1] == board[2][1]) or (board[0][2] == board[1][2] == board[2][2]) or (
                    board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        print('Ничья. Игра окончена.')
        return True


def check_win():  # делаем проверку на победу одного из игроков
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        print('Игрок 1(X) победил по горизонтали 1|2|3')
        print('Игра окончена.')
        return True
    elif board[1][0] == board[1][1] == board[1][2] == 'X':
        print('Игрок 1(X) победил по горизонтали 4|5|6')
        print('Игра окончена.')
        return True
    elif board[2][0] == board[2][1] == board[2][2] == 'X':
        print('Игрок 1(X) победил по горизонтали 7|8|9')
        print('Игра окончена.')
        return True
    elif board[0][0] == board[1][0] == board[2][0] == 'X':
        print('Игрок 1(X) победил по вертикали 1|4|7')
        print('Игра окончена.')
        return True
    elif board[0][1] == board[1][1] == board[2][1] == 'X':
        print('Игрок 1(X) победил по вертикали 2|5|8')
        print('Игра окончена.')
        return True
    elif board[0][2] == board[1][2] == board[2][2] == 'X':
        print('Игрок 1(X) победил по вертикали 3|6|9')
        print('Игра окончена.')
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        print('Игрок 1(X) победил по диагонали 1|5|9')
        print('Игра окончена.')
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'X':
        print('Игрок 1(X) победил по диагонали 3|5|7')
        print('Игра окончена.')
        return True
    elif board[0][0] == board[0][1] == board[0][2] == 'O':
        print('Игрок 2(O) победил по горизонтали 1|2|3')
        print('Игра окончена.')
        return True
    elif board[1][0] == board[1][1] == board[1][2] == 'O':
        print('Игрок 2(O) победил по горизонтали 4|5|6')
        print('Игра окончена.')
        return True
    elif board[2][0] == board[2][1] == board[2][2] == 'O':
        print('Игрок 2(O) победил по горизонтали 7|8|9')
        print('Игра окончена.')
        return True
    elif board[0][0] == board[1][0] == board[2][0] == 'O':
        print('Игрок 2(O) победил по вертикали 1|4|7')
        print('Игра окончена.')
        return True
    elif board[0][1] == board[1][1] == board[2][1] == 'O':
        print('Игрок 2(O) победил по вертикали 2|5|8')
        print('Игра окончена.')
        return True
    elif board[0][2] == board[1][2] == board[2][2] == 'O':
        print('Игрок 2(O) победил по вертикали 3|6|9')
        print('Игра окончена.')
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        print('Игрок 2(O) победил по диагонали 1|5|9')
        print('Игра окончена.')
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        print('Игрок 2(O) победил по диагонали 3|5|7')
        print('Игра окончена.')
        return True


draw_board()
while True:  # для удобства окончания игры создает бесконечный цикл while, начинаем игру
    attempt_generationx()  # 1 ход
    attempt_generation0()  # 2 ход
    attempt_generationx()  # 3 ход
    attempt_generation0()  # 4 ход
    attempt_generationx()  # 5 ход
    if check_win():  # делаем проверку на победу после пятого хода, т.к. до этого хода это делать бессмысленно
        break
    attempt_generation0()
    if check_win():
        break
    attempt_generationx()
    if check_win():
        break
    attempt_generation0()
    if check_win():
        break
    attempt_generationx()  # 9 (последний) ход
    if check_win() or check_draw():  # после последнего хода проверяем, будет ли в итоге победа, или же игра закончится ничьей.
        break
