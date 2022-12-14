"""
Вариант №4
Про удалённость прямоугольников
Работу выполнил Хаметов Д.С.
студент группы КИ22-17/1б
"""
from math import sqrt


def cg_distance(a, c, a1, c1) -> float:
    # Функция для нахождения расстояния между центрами тяжести
    # двух прямоугольников
    list1 = list((a, c, a1, c1))
    x = (list1[0][0] + list1[1][0]) / 2
    y = (list1[0][1] + list1[1][1]) / 2
    x2 = ((list1[2][0] + list1[3][0]) / 2)
    y2 = ((list1[2][1] + list1[3][1]) / 2)
    return sqrt((x2 - x) ** 2 + (y2 - y) ** 2)


def vvod():
    a = tuple(input().split())
    return a


def tpl(a):
    res = tuple(float(i) for i in a)
    return res


def corner_distance(b, b1, d, d1) -> float:
    # Функция для нахождения суммы растояний между верхними
    # левыми и нижними правыми углами двух прямоугольников
    list1 = [b, b1, d, d1]
    x1 = list1[0][0]
    x2 = list1[1][0]
    y1 = list1[0][1]
    y2 = list1[1][1]
    x3 = list1[2][0]
    x4 = list1[3][0]
    y3 = list1[2][1]
    y4 = list1[3][1]
    res = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    return res


def menu():
    # Вывод меню для пользователя
    print('[1] Для нахождения расстояния между центрами тяжести двух прямоугольников\n'
          'введите "option 1"\n'
          '[2] Для нахождения суммы растояний между верхними левыми и нижними правыми углами\n'
          'двух прямоугольников введите "option 2"\n'

          'Для выхода из программы введите "end"\n'
          'Для ввода новых прямоугольников введите "new"'
          )


while True:
    print('Введите координаты противоположных сторон первого, затем второго прямоугольников\n'
          'Пример: Сторону a с координатами (5;1) следует ввести так - 5 1')
    a = vvod()
    c = vvod()
    a1 = vvod()
    c1 = vvod()
    print('Введите координаты левых верхних сторон прямоугольников\n'
          'Затем введите координаты правых нижних')
    b = vvod()
    b1 = vvod()
    d = vvod()
    d1 = vvod()

    try:
        a = tpl(a)
        c = tpl(c)
        a1 = tpl(a1)
        c1 = tpl(c1)

        b = tpl(b)
        b1 = tpl(b1)
        d = tpl(d)
        d1 = tpl(d1)
    except ValueError:
        print('Некорректный ввод!')
        continue
    menu()
    while True:
        choise = input('Выберите опцию ')
        if choise == 'option 1':
            print(cg_distance(a, c, a1, c1))
        elif choise == 'option 2':
            print(corner_distance(b, b1, d, d1))
        elif choise == 'end':
            raise SystemExit
        elif choise == 'new':
            break
        else:
            print('incorrect input')
