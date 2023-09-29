from random import randint


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class FieldEx(Exception):
    pass


class FieldOutEx(FieldEx):
    def __str__(self):
        return "Нельзя стрелять за пределы поля!"


class FieldRepeatEx(FieldEx):
    def __str__(self):
        return "Ты уже стрелял по этой клетке!"


class FieldWrongPlaceEx(FieldEx):
    pass


class Ship:
    def __init__(self, bow, length, direction):
        self.bow = bow
        self.length = length
        self.direction = direction
        self.health = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            current_x = self.bow.x
            current_y = self.bow.y

            if self.direction == 0:
                current_x += i

            elif self.direction == 1:
                current_y += i

            ship_dots.append(Dot(current_x, current_y))

        return ship_dots

    def shooted(self, shot):
        return shot in self.dots


class Color:

    yellow = '\033[93m'
    yellowB = '\033[1;93m'
    redB = '\033[1;91m'
    purple = '\033[95m'
    purpleB = '\033[1;95m'
    purple2 = '\033[35m'
    purple2B = '\033[1;35m'
    turquoise2B = '\033[1;36m'
    blueB = '\033[1;94m'
    blue2B = '\033[1;34m'
    reset = '\033[0m'


def set_color(letter, color):
    return color + letter + Color.reset


class Field:
    def __init__(self, hide=False, size=10):
        self.hide = hide
        self.size = size
        self.count = 0
        self.field = [["_"] * size for _ in range(self.size)]
        self.busy = []
        self.ships = []

    def add_ships(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise FieldWrongPlaceEx()
        for dot in ship.dots:
            self.field[dot.x][dot.y] = set_color("■", Color.blueB)
            self.busy.append(dot)

        self.ships.append(ship)
        self.contours(ship)

    def contours(self, ship, choice=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot in ship.dots:
            for dx, dy in near:
                current = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(current)) and current not in self.busy:
                    if choice:
                        self.field[current.x][current.y] = set_color("•", Color.yellow)
                    self.busy.append(current)

    def __str__(self):
        result = set_color("•", Color.purpleB)
        result += " | \033[32m0\033[0m | \033[32m1\033[0m | \033[32m2\033[0m | \033[32m3\033[0m | \033[32m4\033[0m |" \
                  " \033[32m5\033[0m | \033[32m6\033[0m | \033[32m7\033[0m | \033[32m8\033[0m | \033[32m9\033[0m |"
        for i, row in enumerate(self.field):
            result += f"\033[32m\n{i}\033[0m | " + " | ".join(row) + " |"

        if self.hide:
            result = result.replace("■", "\033[0m_")
        return result

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise FieldOutEx()

        if dot in self.busy:
            raise FieldRepeatEx()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.health -= 1
                self.field[dot.x][dot.y] = set_color("X", Color.redB)
                if ship.health == 0:
                    self.count += 1
                    self.contours(ship, choice=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[dot.x][dot.y] = set_color("•", Color.yellow)
        print("Мимо!")
        return False

    def start(self):
        self.busy = []


class Player:
    def __init__(self, field, enemy):
        self.field = field
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except FieldEx as e:
                print(e)


class Computer(Player):
    def __init__(self, field, enemy):
        super().__init__(field, enemy)
        self.last_hit = None

    def ask(self):
        if self.last_hit:
            targets_around = [
                Dot(self.last_hit.x + 1, self.last_hit.y),
                Dot(self.last_hit.x - 1, self.last_hit.y),
                Dot(self.last_hit.x, self.last_hit.y + 1),
                Dot(self.last_hit.x, self.last_hit.y - 1)
            ]
            target = targets_around[randint(0, len(targets_around) - 1)]
            print(f"Компьютер стреляет в: {target.x} {target.y}")
            return target
        else:
            target = Dot(randint(0, 8), randint(0, 8))
            print(f"Компьютер стреляет в: {target.x} {target.y}")
            return target


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()
            if len(cords) != 2:
                print("Введите 2 координаты!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа!")
                continue

            x, y = int(x), int(y)

            return Dot(x, y)


class Game:
    def __init__(self, size=10):
        self.size = size
        self.manual_placement = False

        pl = self.manual_field_placement() if self.manual_placement else self.random_field()
        co = self.random_field()
        co.hide = True

        self.computer = Computer(co, pl)
        self.us = User(pl, co)

    def manual_field_placement(self):
        print("Ручная расстановка кораблей.")
        field = Field(size=self.size)
        for length in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
            while True:
                try:
                    print(field)
                    print(f"Размещение корабля длиной {length}")
                    x, y = map(int, input("Введите координаты (x y): ").split())
                    direction = int(input("Выберите направление (0 - вертикально, 1 - горизонтально): "))
                    ship = Ship(Dot(x, y), length, direction)
                    field.add_ships(ship)
                    break
                except FieldWrongPlaceEx:
                    print("Корабль не может быть размещен в данной позиции. Попробуйте снова.")
                field.start()
                return field

        field.start()
        return field

    def random_field(self):
        field = None
        while field is None:
            field = self.random_place()
        return field

    def random_place(self):
        lens = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        field = Field(size=self.size)
        attempts = 0
        for length in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), length, randint(0, 1))
                try:
                    field.add_ships(ship)
                    break
                except FieldWrongPlaceEx:
                    pass
        field.start()
        return field

    def greetings(self, player_name):
        upper_name = player_name.upper()
        print("-" * 60)
        print("|", set_color(f"  {upper_name}, ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'МОРСКОЙ БОЙ'        ".center(60), Color.yellowB),
              "|")
        print("|", set_color(" Правила игры:".ljust(60), Color.blue2B), "|")
        print("|", set_color(" 1. Ваша задача - потопить корабли противника.         ".ljust(60), Color.turquoise2B),
              "|")
        print("|",
              set_color(" 2. Игровое поле представляет из себя квадрат размером 10x10.".ljust(60), Color.turquoise2B),
              "|")
        print("|",
              set_color(" 3. Корабли можно располагать вручную или случайным образом.".ljust(60), Color.turquoise2B),
              "|")
        print("|", set_color(" 4. Доступные корабли: 1x4, 2x3, 3x2, 4x1.               ".ljust(60), Color.turquoise2B),
              "|")
        print("|", set_color(" 5. Компьютер будет стрелять ваши корабли на своем поле.  ".ljust(60), Color.turquoise2B),
              "|")
        print("|", set_color(" 6. Удачи в бою!                                        ".ljust(60), Color.turquoise2B),
              "|")
        print("-" * 60)

    def loop(self):
        num = 0
        while True:
            print("-" * 43)
            print("|", set_color("                 ИГРОК                 ".center(6), Color.blue2B), "|")
            print("-" * 43)
            print(self.us.field)
            print("-" * 43)
            print("|", set_color("               КОМПЬЮТЕР               ".center(6), Color.redB), "|")
            print("-" * 43)
            print(self.computer.field)
            if num % 2 == 0:
                print("-" * 43)
                print("              ( Ход игрока )                ".center(6))
                print("-" * 43)
                repeat = self.us.move()
            else:
                print("-" * 43)
                print("            ( Ход компьютера )             ".center(6))
                print("-" * 43)
                repeat = self.computer.move()
            if repeat:
                num -= 1

            if self.computer.field.count == 7:
                print("-" * 43)
                print("Игрок выиграл!")
                break

            if self.us.field.count == 7:
                print("-" * 43)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        player_name = input("Введите ваше имя: ")
        self.greetings(player_name)
        placement_choice = input("Хотите разместить корабли вручную? (да/нет): ")
        if placement_choice.lower() == 'да':
            self.manual_placement = True
            self.manual_field_placement()
        self.loop()


g = Game()
g.manual_placement = True
g.start()
