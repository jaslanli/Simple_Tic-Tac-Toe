class TicTacToe:
    x_o = ["_" for value in range(0, 9)]
    matrix = [[x_o[0], x_o[1], x_o[2]], [x_o[3], x_o[4], x_o[5]], [x_o[6], x_o[7], x_o[8]]]
    move_list = []

    def __init__(self):
        self.x = None
        self.y = None
        self.columns = None
        self.diagonals = None

    def grid(self):
        print("---------")
        print(f"| {self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]} |")
        print(f"| {self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]} |")
        print(f"| {self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]} |")
        print("---------")

    def move(self, pawn):
        x, y = input().split()
        try:
            if x.isdigit() and y.isdigit():
                index = 3 * int(x) + int(y) - 4
                if self.x_o[index] == "_":
                    self.x_o[index] = pawn
                x = int(x) - 1
                y = int(y) - 1
            if not (0 <= x <= 2 and 0 <= y <= 2):
                print("Coordinates should be from 1 to 3!")
            else:
                if self.matrix[x][y] == "_":
                    self.matrix[x][y] = pawn
                    self.grid()
                else:
                    print("This cell is occupied! Choose another one!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")

        self.columns = [[self.x_o[0], self.x_o[3], self.x_o[6]], [self.x_o[1], self.x_o[4], self.x_o[7]], [self.x_o[2], self.x_o[5], self.x_o[8]]]
        self.diagonals = [[self.x_o[0], self.x_o[4], self.x_o[8]], [self.x_o[2], self.x_o[4], self.x_o[6]]]

    def victory(self):
        for row in self.matrix:
            if row.count("X") == 3:
                print("X wins")
                exit()
            elif row.count("O") == 3:
                print("O wins")
                exit()
        for column in self.columns:
            if column.count("X") == 3:
                print("X wins")
                exit()
            elif column.count("O") == 3:
                print("O wins")
                exit()
        for diagonal in self.diagonals:
            if diagonal.count("X") == 3:
                print("X wins")
                exit()
            elif diagonal.count("O") == 3:
                print("O wins")
                exit()

    def play_game(self):
        self.grid()
        while True:
            self.move("X")
            self.move_list.append("X")
            if self.victory():
                print(self.victory)
                break
            elif self.move_list.count("X") + self.move_list.count("O") > 9:
                print("Draw")
                break
            else:
                self.move("O")
                self.move_list.append("O")
                if self.victory():
                    print(self.victory)
                    break
                elif len(self.move_list) == 9 and self.victory() is False:
                    print("Draw")
                    break


tictactoe = TicTacToe()
tictactoe.play_game()
