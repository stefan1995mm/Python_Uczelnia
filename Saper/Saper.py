import random


def get_number_of_mines():
    number_of_mines = int(input('Podaj liczbę min: '))
    return number_of_mines


def deploy_mines(mines, size):
    x = []
    y = []
    for a in range(mines):
        x.append(random.randint(0, size - 1))
        y.append(random.randint(0, size - 1))
    return (x, y)


def number_of_nieghboring_mines(x, y, board):
    count = 0
    if board[x][y] == 9:
        return 9
    size = len(board)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if -1 < (x + i) < size and -1 < (y + j) < size:
                if board[x + i][y + j] == 9:
                    count += 1
                else:
                    continue

    return count


def create_board(x, size):
    board = [[0] * size for i in range(size)]
    player_view = [[0] * size for i in range(size)]
    i = 0
    for i in range(len(x[0])):
        board[x[0][i]][x[1][i]] = 9
    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            c = number_of_nieghboring_mines(i, j, board)
            board[i][j] = c
    return (player_view, board)


def print_board(player_board, board, size):
    result = True
    counter_x = 0
    counter_y = 0
    print("x y", end="")
    for i_y in range(size):
        print(counter_y, end=" ")
        if counter_y < 10:
            print("", end=" ")
        counter_y += 1
    print("")
    for i_x in range(size):
        print(counter_x, end=" ")
        counter_x += 1
        if counter_x < 10:
            print(" ", end="")
        for i_y in range(size):

            if player_board[i_x][i_y]:
                if board[i_x][i_y] == 9:
                    print("X", end="")
                    result = False
                else:
                    print(board[i_x][i_y], end="")
            else:
                print("_", end="")
            print("  ", end="")
        print("")
    return result


def reveal_squares(player_board, board, x, y, size):
    if player_board[x][y] == 0:
        player_board[x][y] = 1
        if board[x][y] == 0:
            for x_x in range(x - 1, x + 2):
                for y_y in range(y - 1, y + 2):
                    if size > x_x > -1 and size > y_y > -1:
                        player_board = reveal_squares(player_board, board, x_x, y_y, size)
    return player_board


def check_Is_Win(board, mine):
    size = len(board[0])
    fields = (size * size) - mine
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                fields -= 1
                if fields == 0:
                    return True
    return False


def sapper():
    loop = True
    print("Witam w grze saper!!!")
    mines_count = get_number_of_mines()
    size = int(input('Podaj wielkosc planszy(kwadrat): '))
    mines_xy = deploy_mines(mines_count, size)
    boards = create_board(mines_xy, size)
    player_ = boards[0]
    b_mines = boards[1]
    print_board(boards[0], boards[1], size)
    while (loop == True):
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))
        player_ = reveal_squares(player_, b_mines, y, x, size)
        loop = print_board(boards[0], boards[1], size)
        counter = check_Is_Win(player_, mines_count)
        if (counter):
            print("wygrałeś")
            break
    print("koniec gry")


sapper()
