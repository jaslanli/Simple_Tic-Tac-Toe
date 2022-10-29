a = "         "
b = list(a)

def grid():
    print("---------")
    print("|", b[0], b[1], b[2], "|")
    print("|", b[3], b[4], b[5], "|")
    print("|", b[6], b[7], b[8], "|")
    print("---------")

grid()

def x_win():
    if b[0] + b[1] + b[2] == 'XXX':
        return "X wins"
    elif b[3] + b[4] + b[5] == 'XXX':
        return "X wins"
    elif b[6] + b[7] + b[8] == 'XXX':
        return "X wins"
    elif b[0] + b[3] + b[6] == 'XXX':
        return "X wins"
    elif b[1] + b[4] + b[7] == 'XXX':
        return "X wins"
    elif b[2] + b[5] + b[8] == 'XXX':
        return "X wins"
    elif b[0] + b[4] + b[8] == 'XXX':
        return "X wins"
    elif b[2] + b[4] + b[6] == 'XXX':
        return "X wins"

def o_win():
    if b[0] + b[1] + b[2] == 'OOO':
        return "O wins"
    elif b[3] + b[4] + b[5] == 'OOO':
        return "O wins"
    elif b[6] + b[7] + b[8] == 'OOO':
        return "O wins"
    elif b[0] + b[3] + b[6] == 'OOO':
        return "O wins"
    elif b[1] + b[4] + b[7] == 'OOO':
        return "O wins"
    elif b[2] + b[5] + b[8] == 'OOO':
        return "O wins"
    elif b[0] + b[4] + b[8] == 'OOO':
        return "O wins"
    elif b[2] + b[4] + b[6] == 'OOO':
        return "O wins"

x_count = 0
o_count = 0

while x_count + o_count < 9:
    while x_count < 5:
        user_input = input()
        x = user_input.split()[0]
        y = user_input.split()[-1]
        if x.isnumeric() is not True and y.isnumeric() is not True:
            print("You should enter numbers!")
        elif 1 > int(x) or int(x) > 3 or 1 > int(y) or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
        elif 1 < int(x) or int(x) < 3 or 1 < int(y) or int(y) < 3:
            new_grid = (((int(x) - 1) * 3) + (int(y) + 2)) - 3
            if b[new_grid] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                b[new_grid] = "X"
                grid()
                x_count += 1
                break

    if x_win() is not None:
        print(x_win())
        break

    while o_count < 4:
        user_input = input()
        x = user_input.split()[0]
        y = user_input.split()[-1]
        if x.isnumeric() is not True and y.isnumeric() is not True:
            print("You should enter numbers!")
        elif 1 > int(x) or int(x) > 3 or 1 > int(y) or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
        elif 1 < int(x) or int(x) < 3 or 1 < int(y) or int(y) < 3:
            new_grid = (((int(x) - 1) * 3) + (int(y) + 2)) - 3
            if b[new_grid] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                b[new_grid] = "O"
                grid()
                o_count += 1
                break

    if o_win() is not None:
        print(o_win())
        break

else:
    print("Draw")
