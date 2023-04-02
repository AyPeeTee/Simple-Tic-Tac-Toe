o_win = False
x_win = False
count = 0
player = "X"
grid = ["---------"], \
    ["|", "_", "_", "_", "|"], \
    ["|", "_", "_", "_", "|"], \
    ["|", "_", "_", "_", "|"], \
    ["---------"]


def draw():
    print("\n".join(" ".join(str(el) for el in row) for row in grid))


def checkWin(x):
    global o_win
    global x_win
    if grid[1][1] == player and grid[1][2] == player and grid[1][3] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[1][1] == player and grid[2][1] == player and grid[3][1] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[2][1] == player and grid[2][2] == player and grid[2][3] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[1][2] == player and grid[2][2] == player and grid[3][2] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[3][1] == player and grid[3][2] == player and grid[3][3] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[1][3] == player and grid[2][3] == player and grid[3][3] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[1][1] == player and grid[2][2] == player and grid[3][3] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True
    elif grid[1][3] == player and grid[2][2] == player and grid[3][1] == player:
        if player == "X":
            x_win = True
        else:
            o_win = True


def print_win():
    if x_win:
        print("X wins")
    elif o_win:
        print("O wins")


while True:
    draw()
    user_cord = input().replace(" ", "")
    if user_cord.isnumeric():
        cord1 = int(user_cord[0])
        cord2 = int(user_cord[1])
        if (cord1 >= 1) and (cord1 <= 3) and (cord2 >= 1) and (cord2 <= 3):
            if grid[cord1][cord2] == "_":
                grid[cord1][cord2] = player
                count += 1
                checkWin(player)
                if x_win or o_win:
                    draw()
                    print_win()
                    break
                elif (count == 9) and (not x_win) and (not o_win):
                    draw()
                    print("Draw")
                    break
                if player == "O":
                    player = "X"
                else:
                    player = "O"
                continue
            else:
                if count == 10:
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("You should enter numbers!")
        continue
