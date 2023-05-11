#Морской бой
import random

ai_ship_dots = []
pl_ship_dots = []
ai_shots = []
pl_shots = []
pl_life = 11
ai_life = 11
dots = []
exceptions = []
dots_3 = []
exceptions_3 = []
dots_2 = []
exceptions_2 = []
dots_1 = []
exceptions_1 = []
direction = []
c = 0

print()
print("     Приветсвуем вас в игре морской бой! ")
print()
field = [[" "] * 6 for i in range(6)]
print('     Доска')
print()
print("    | 0 | 1 | 2 | 3 | 4 | 5 | ")
for i, row in enumerate(field):
    row_str = f"  {i} | {' | '.join(row)} | "
    print(row_str)
print()


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


d = Dot


class Ship:
    def __init__(self, dots, exceptions):
        self.dots = dots
        self.exceptions = exceptions

    def add_ship(self, length, d, direction):
        self.length = length
        self.d = d
        self.direction = direction

        d = Dot(random.randint(0, 3), random.randint(0, 3))
        direction = random.choice(['vertical', 'horizontal'])
        if length == 3:
            if direction == 'vertical':
                dots_3.extend([d, Dot(d.x, d.y + 1), Dot(d.x, d.y + 2)])
                exceptions_3.extend( #добавлем контур
                    [Dot(d.x, d.y - 1), Dot(d.x - 1, d.y - 1), Dot(d.x + 1, d.y - 1),
                     Dot(d.x - 1, d.y), Dot(d.x + 1, d.y), Dot(d.x - 1, d.y + 1),
                     Dot(d.x + 1, d.y + 1), Dot(d.x - 1, d.y + 2), Dot(d.x + 1, d.y + 2),
                     Dot(d.x, d.y + 3), Dot(d.x - 1, d.y + 3), Dot(d.x + 1, d.y + 3)])
                return dots_3, exceptions_3
            else:
                dots_3.extend([d, Dot(d.x + 1, d.y), Dot(d.x + 2, d.y)])
                exceptions_3.extend(
                    [Dot(d.x - 1, d.y), Dot(d.x - 1, d.y - 1), Dot(d.x - 1, d.y + 1),
                     Dot(d.x, d.y - 1), Dot(d.x, d.y + 1), Dot(d.x + 1, d.y - 1),
                     Dot(d.x + 1, d.y + 1), Dot(d.x + 2, d.y - 1), Dot(d.x + 2, d.y + 1),
                     Dot(d.x + 3, d.y), Dot(d.x + 3, d.y + 1), Dot(d.x + 3, d.y - 1)])
                return dots_3, exceptions_3
        elif length == 2:
            while True:
                d = Dot(random.randint(0, 4), random.randint(0, 4))
                direction = random.choice(['vertical', 'horizontal'])
                if direction == 'vertical':  # проверка вхождений точек нового корабля в других кораблях и их контурах
                    if d not in exceptions_3 and d not in dots_3 and Dot(d.x, d.y + 1) not in exceptions_3 \
                            and Dot(d.x, d.y + 1) not in dots_3 and d not in exceptions_2 and d not in dots_2 \
                            and Dot(d.x, d.y + 1) not in exceptions_2 and Dot(d.x, d.y + 1) not in dots_2:
                        dots_2.extend([d, Dot(d.x, d.y + 1)])
                        exceptions_2.extend(
                            [Dot(d.x, d.y - 1), Dot(d.x - 1, d.y - 1), Dot(d.x + 1, d.y - 1), Dot(d.x - 1, d.y),
                             Dot(d.x + 1, d.y), Dot(d.x - 1, d.y + 1), Dot(d.x + 1, d.y + 1), Dot(d.x, d.y + 2),
                             Dot(d.x - 1, d.y + 2), Dot(d.x + 1, d.y + 2)])
                        return dots_2, exceptions_2
                else:
                    if d not in exceptions_3 and d not in dots_3 and Dot(d.x + 1, d.y) not in exceptions_3 \
                            and Dot(d.x + 1, d.y) not in dots_3 and d not in exceptions_2 and d not in dots_2 \
                            and Dot(d.x + 1, d.y) not in exceptions_2 and Dot(d.x + 1, d.y) not in dots_2:
                        dots_2.extend([d, Dot(d.x + 1, d.y)])
                        exceptions_2.extend(
                            [Dot(d.x - 1, d.y), Dot(d.x - 1, d.y - 1), Dot(d.x - 1, d.y + 1), Dot(d.x, d.y - 1),
                             Dot(d.x, d.y + 1), Dot(d.x + 1, d.y - 1), Dot(d.x + 1, d.y + 1), Dot(d.x + 2, d.y),
                             Dot(d.x + 2, d.y - 1), Dot(d.x + 2, d.y + 1)])
                        return dots_2, exceptions_2
        else:
            f = 0
            while True:
                d = Dot(random.randint(0, 5), random.randint(0, 5))
                f += 1
                if f > 100:
                    break
                if d not in exceptions_3 and d not in dots_3 and d not in exceptions_2 and d not in dots_2 \
                        and d not in exceptions_1 and d not in dots_1:
                    dots_1.append(d)
                    exceptions_1.extend([
                        Dot(d.x, d.y - 1), Dot(d.x - 1, d.y - 1), Dot(d.x + 1, d.y - 1), Dot(d.x - 1, d.y),
                        Dot(d.x + 1, d.y), Dot(d.x, d.y + 1), Dot(d.x - 1, d.y + 1), Dot(d.x + 1, d.y + 1)])
                    return dots_1, exceptions_1


class Board:
    def __init__(self, b_dots):
        self.b_dots = b_dots

#собираем доску игрока
while True:

    pl_s3 = Ship(dots, exceptions).add_ship(3, d, direction)
    pl_s2_1 = Ship(dots, exceptions).add_ship(2, d, direction)
    pl_s2_2 = Ship(dots, exceptions).add_ship(2, d, direction)
    pl_s1_1 = Ship(dots, exceptions).add_ship(1, d, direction)
    pl_s1_2 = Ship(dots, exceptions).add_ship(1, d, direction)
    pl_s1_3 = Ship(dots, exceptions).add_ship(1, d, direction)
    pl_s1_4 = Ship(dots, exceptions).add_ship(1, d, direction)

    if pl_s1_1 is None or pl_s1_2 is None or pl_s1_3 is None or pl_s1_4 is None:
        dots_3.clear(), dots_2.clear(), dots_1.clear(), exceptions_3.clear(), exceptions_2.clear(), exceptions_1.clear()
        continue

    pl_s3 = [[pl_s3[0][0], pl_s3[0][1], pl_s3[0][2]], pl_s3[1][:12]]
    pl_s2_1 = [[pl_s2_1[0][0], pl_s2_1[0][1]], pl_s2_1[1][:10]]
    pl_s2_2 = [[pl_s2_2[0][2], pl_s2_2[0][3]], pl_s2_2[1][10:]]
    pl_s1_1 = [[pl_s1_1[0][0]], pl_s1_1[1][:8]]
    pl_s1_2 = [[pl_s1_2[0][1]], pl_s1_2[1][8:16]]
    pl_s1_3 = [[pl_s1_3[0][2]], pl_s1_3[1][16:24]]
    pl_s1_4 = [[pl_s1_4[0][3]], pl_s1_4[1][24:]]

    pl_ship_dots = pl_s3[0] + pl_s2_1[0] + pl_s2_2[0] + pl_s1_1[0] + pl_s1_2[0] + pl_s1_3[0] + pl_s1_4[0]
    dots_3.clear(), dots_2.clear(), dots_1.clear(), exceptions_3.clear(), exceptions_2.clear(), exceptions_1.clear()
    break

#собираем доску ии
while True:

    ai_s3 = Ship(dots, exceptions).add_ship(3, d, direction)
    ai_s2_1 = Ship(dots, exceptions).add_ship(2, d, direction)
    ai_s2_2 = Ship(dots, exceptions).add_ship(2, d, direction)
    ai_s1_1 = Ship(dots, exceptions).add_ship(1, d, direction)
    ai_s1_2 = Ship(dots, exceptions).add_ship(1, d, direction)
    ai_s1_3 = Ship(dots, exceptions).add_ship(1, d, direction)
    ai_s1_4 = Ship(dots, exceptions).add_ship(1, d, direction)

    if ai_s1_1 is None or ai_s1_2 is None or ai_s1_3 is None or ai_s1_4 is None:
        dots_3. clear(), dots_2.clear(), dots_1.clear(), exceptions_3.clear(), exceptions_2.clear(), exceptions_1.clear()
        continue

    ai_s3 = [[ai_s3[0][0], ai_s3[0][1], ai_s3[0][2]], ai_s3[1][:12]]
    ai_s2_1 = [[ai_s2_1[0][0], ai_s2_1[0][1]], ai_s2_1[1][:10]]
    ai_s2_2 = [[ai_s2_2[0][2], ai_s2_2[0][3]], ai_s2_2[1][10:]]
    ai_s1_1 = [[ai_s1_1[0][0]], ai_s1_1[1][:8]]
    ai_s1_2 = [[ai_s1_2[0][1]], ai_s1_2[1][8:16]]
    ai_s1_3 = [[ai_s1_3[0][2]], ai_s1_3[1][16:24]]
    ai_s1_4 = [[ai_s1_4[0][3]], ai_s1_4[1][24:]]

    ai_ship_dots = ai_s3[0] + ai_s2_1[0] + ai_s2_2[0] + ai_s1_1[0] + ai_s1_2[0] + ai_s1_3[0] + ai_s1_4[0]
    dots_3.clear(), dots_2.clear(), dots_1.clear(), exceptions_3.clear(), exceptions_2.clear(), exceptions_1.clear()
    break

while True:
    if ai_life == 0:
        print('Игрок победил!')
        break
    if pl_life == 0:
        print('ИИ победил!')
        break
    print('Ход игрока')
    sh = input('Введите через пробел 2 числа координаты хода по осям x,y (например 1 2) :')
    shot = sh.split(' ')

    if ' ' not in sh:
        print('Через пробел')
        continue

    try:
        pl_shot = Dot(int(shot[0]), int(shot[1]))
    except ValueError:
        print('Ошибка ввода')
        continue

    if pl_shot.x > 5 or pl_shot.x < 0 or pl_shot.y > 5 or pl_shot.y < 0:
        print('Выход за пределы доски')
        continue

    if pl_shot not in pl_shots:
        pl_shots.append(pl_shot)
    else:
        print('Вы уже стреляли в эту клетку')
        continue

    if pl_shot in ai_ship_dots:
        ai_life -= 1
        print('Игрок попал')
        print()
        for i in ai_s3[0], ai_s2_1[0], ai_s2_2[0], ai_s1_1[0], ai_s1_2[0], ai_s1_3[0], ai_s1_4[0]:
            try:
                i.remove(pl_shot) #удаляем точку из списка у подбитого корабля ии
            except ValueError:
                continue
    else:
        while True:
            ai_shot = Dot(random.randint(0, 5), random.randint(0, 5))
            if ai_shot in ai_shots:
                continue
            else:
                print('Ход ИИ:', ai_shot.x, ai_shot.y)
                ai_shots.append(ai_shot)
            if ai_shot in pl_ship_dots:
                print('ИИ попал')
                pl_life -= 1
                if pl_life == 0:
                    break
                for i in pl_s3[0], pl_s2_1[0], pl_s2_2[0], pl_s1_1[0], pl_s1_2[0], pl_s1_3[0], pl_s1_4[0]:
                    try:
                        i.remove(ai_shot)  # удаляем точку из списка у подбитого корабля игрока
                    except ValueError:
                        continue
                continue
            else:
                break

    pl_board = Board(pl_ship_dots)
    pl_field = [[" "] * 6 for i in range(6)]
    for pl_ship_cord in pl_board.b_dots:
        pl_field[pl_ship_cord.x][pl_ship_cord.y] = '■'
    for l in pl_s3, pl_s2_1, pl_s2_2, pl_s1_1, pl_s1_2, pl_s1_3, pl_s1_4:
        if len(l[0]) == 0:  # если длина списка точек корабля = 0, то проходимся по его контуру
            for c in range(12):
                try:
                    if l[1][c].x < 0 or l[1][c].x > 5 or l[1][c].y < 0 or l[1][c].y > 5:
                        c += 1
                    else:
                        pl_field[l[1][c].x][l[1][c].y] = '.'
                        ai_shots.append(Dot(l[1][c].x, l[1][c].y)) #добавляем контур в список выстрелов ии
                        c += 1
                        continue
                except:
                    IndexError()

    for pl_ship_cord in ai_shots:
        pl_field[pl_ship_cord.x][pl_ship_cord.y] = '.'
    for pl_ship_cord in pl_board.b_dots:
        if pl_ship_cord in ai_shots:
            pl_field[pl_ship_cord.x][pl_ship_cord.y] = 'X'
    print('     Доска игрока')
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | ")
    for i, pl_row in enumerate(pl_field):
        pl_row_str = f"  {i} | {' | '.join(pl_row)} | "
        print(pl_row_str)

    ai_board = Board(ai_ship_dots)
    ai_field = [[" "] * 6 for j in range(6)]
    for ai_ship_cord in pl_shots:
        ai_field[ai_ship_cord.x][ai_ship_cord.y] = '.'
    for ai_ship_cord in ai_board.b_dots:
        if ai_ship_cord in pl_shots:
            ai_field[ai_ship_cord.x][ai_ship_cord.y] = 'X'
    for l in ai_s3, ai_s2_1, ai_s2_2, ai_s1_1, ai_s1_2, ai_s1_3, ai_s1_4:
        if len(l[0]) == 0:  # если длина списка точек корабля = 0, то проходимся по его контуру
            for c in range(12):
                try:
                    if l[1][c].x < 0 or l[1][c].x > 5 or l[1][c].y < 0 or l[1][c].y > 5:
                        c += 1
                    else:
                        ai_field[l[1][c].x][l[1][c].y] = '.'
                        pl_shots.append(Dot(l[1][c].x, l[1][c].y)) #добавляем контур в список выстрелов игрока
                        c += 1
                except:
                    IndexError()

    print('     Доска ИИ')
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | ")
    for j, ai_row in enumerate(ai_field):
        ai_row_str = f"  {j} | {' | '.join(ai_row)} | "
        print(ai_row_str)
    print()
    if pl_shot in ai_ship_dots:
        continue
