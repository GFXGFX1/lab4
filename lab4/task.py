backpack = [[], [], [], [], [], [], [], [], []]  # список списков
items = {
    'r': (3, 25),  # винтовка
    'p': (2, 15),  # пистолет
    'a': (2, 15),  # боекомплект
    'm': (2, 20),  # фптечка
    'i': (1, 5),  # ингалятор
    'k': (1, 15),  # нож
    'x': (3, 20),  # топор
    't': (1, 25),  # оберег
    'f': (1, 15),  # фляжка
    'd': (1, 10),  # антидот
    's': (2, 20),  # еда
    'c': (2, 20)  # арбалет
}  # rjhnt;b


def task(items, inv=9):
    bp_task = [[0] * (inv + 1) for i in range(len(items) + 1)] #споиско списков, пока что только с 0
    # print(bp_task)
    # таблица
    for row, (weight, value) in enumerate(items.values(),
                                          1):  # enumerate начинает с 1, что удлбно, ведь остаются ячейки с 0
        for place in range(inv + 1):
            if weight <= place:
                bp_task[row][place] = max(bp_task[row - 1][place],
                                          bp_task[row - 1][place - weight] + value)  # находим максимум
            else:
                bp_task[row][place] = bp_task[row - 1][place]  # оставляем верхнее значение
    # print(bp_task)
    # готовый список-таблица
    # заполняем ячейки рюкзака
    keys = list(items.keys()) # все буквы предметов
    place2 = inv
    slot = 0
    for row2 in range(len(items), 0, -1):
        if bp_task[row2][place2] != bp_task[row2 - 1][place2]:
            key = keys[row2 - 1]
            found = items[key][0]
            for _ in range(found):
                backpack[slot].append(key)
                slot += 1
            place2 -= found # вычитаем
    # cчитаем итоговые очки: взятые - невзятые + начальные (10)
    taken_points = bp_task[-1][-1] #bnjujdst jxrb
    total_points = sum(v for w, v in items.values())  # сумма очков вообще всех предметов
    not_taken_points = total_points - taken_points  # сумма очков невзятых
    return 10 + taken_points - not_taken_points


points = task(items)
# Вывод рюкзака сеткой 3x3
for i in range(0, 9, 3):
    print(backpack[i], backpack[i + 1], backpack[i + 2])  # принтуется сразу 3 ячейки, затем спускается вниз
print(points)
