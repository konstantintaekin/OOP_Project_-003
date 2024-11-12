from random import randint


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple(tuple(Cell() for columns in range(3)) for rows in range(3))

    def __getitem__(self, item):
        i, j = item[0], item[1]
        if isinstance(i, int) and 0 <= i <= 2 and isinstance(j, int) and 0 <= j <= 2:
            return self.pole[i][j].value
        else:
            raise IndexError('некорректно указанные индексы')

    def __setitem__(self, key, value):
        i, j = key[0], key[1]
        if isinstance(i, int) and 0 <= i <= 2 and isinstance(j, int) and 0 <= j <= 2:
            self.pole[i][j].value = value
        else:
            raise IndexError('некорректно указанные индексы')

    def __bool__(self):
        if self.is_human_win:
            return False
        elif self.is_computer_win:
            return False
        elif self.is_draw:
            return False
        else:
            return True

    def init(self):
        #print('Добро пожаловать в игру "Крестики-нолики"')
        for rows in range(len(self.pole)):
            for columns in range(len(self.pole[rows])):
                self.pole[rows][columns].value = self.FREE_CELL

    def show(self):
        for rows in range(4):
            for columns in range(4):
                if rows == 0 and columns == 0:
                    print(' ', end = ' ')
                elif rows == 0 and columns != 0:
                    print(columns - 1, end = ' ')
                elif columns == 0 and rows != 0:
                    print(rows - 1, end = ' ')
                else:
                    if self.pole[rows - 1][columns - 1].value == self.FREE_CELL:
                        print('#', end = ' ')
                    elif self.pole[rows - 1][columns - 1].value == self.HUMAN_X:
                        print('X', end = ' ')
                    elif self.pole[rows - 1][columns - 1].value == self.COMPUTER_O:
                        print('O', end = ' ')
            print()

    def human_go(self):
        while True:
            i, j = map(int, input('Введите координаты свободной ячейки: ').split())
            #if not 0 <= i <= 2 or not 0 <= j <= 2:
                #print('Выход за рамки игрового поля! Попробуйте снова!')
            if self.pole[i][j].value == self.FREE_CELL:
                self.pole[i][j].value = self.HUMAN_X
                break
            #else:
                #print('Данная ячейка занята! Попробуйте снова!')

    def computer_go(self):
        while True:
            i, j = randint(0, 2), randint(0, 2)
            if self.pole[i][j].value == self.FREE_CELL:
                self.pole[i][j].value = self.COMPUTER_O
                break

    def who_win(self, designation):
        win = []
        for rows in self.pole:
            win.append([element.value for element in rows].count(designation) == 3)
        lst_inter = []
        for rows in range(len(self.pole)):
            for columns in range(len(self.pole[rows])):
                lst_inter.append(self.pole[columns][rows])
            win.append([element.value for element in lst_inter].count(designation) == 3)
            lst_inter = []
        win.append([self.pole[0][0].value,  self.pole[1][1].value, self.pole[2][2].value].count(designation) == 3)
        win.append([self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value].count(designation) == 3)
        return any(win)


    @property
    def is_human_win(self):
        return self.who_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.who_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return sum([1 for cell in self.pole for element in cell if element.value == self.FREE_CELL]) == 0


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")