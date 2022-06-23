# -*- coding: utf-8 -*-

import simple_draw as sd
# resolution = (1000, 1000)
# COLOR_YELLOW = (255, 255, 0)
# Start_point = sd.get_point(x=200, y=200)
# Треугольник


# v_1 = sd.get_vector(start_point=Start_point, angle=0, length=200, width=4)
# v_1.draw()
# v_2 = sd.get_vector(start_point=v_1.end_point, angle=120, length=200, width=4)
# v_2.draw()
# v_3 = sd.get_vector(start_point=v_2.end_point, angle=240, length=200, width=4)
# v_3.draw()



# Квадрат
# v_1 = sd.get_vector(start_point=Start_point, angle=0, length=200, width=4)
# v_1.draw()
# v_2 = sd.get_vector(start_point=v_1.end_point, angle=90, length=200, width=4)
# v_2.draw()
# v_3 = sd.get_vector(start_point=v_2.end_point, angle=180, length=200, width=4)
# v_3.draw()
# v_4 = sd.get_vector(start_point=v_3.end_point, angle=270, length=200, width=4)
# v_4.draw()

# Пятиугольник
# v_1 = sd.get_vector(start_point=Start_point, angle=0, length=200, width=4)
# v_1.draw()
# v_2 = sd.get_vector(start_point=v_1.end_point, angle=72, length=200, width=4)
# v_2.draw()
# v_3 = sd.get_vector(start_point=v_2.end_point, angle=144, length=200, width=4)
# v_3.draw()
# v_4 = sd.get_vector(start_point=v_3.end_point, angle=216, length=200, width=4)
# v_4.draw()
# v_5 = sd.get_vector(start_point=v_4.end_point, angle=288, length=200, width=4)
# v_5.draw()

# Шестиугольник
# v_1 = sd.get_vector(start_point=Start_point, angle=0, length=200, width=4)
# v_1.draw()
# v_2 = sd.get_vector(start_point=v_1.end_point, angle=45, length=200, width=4)
# v_2.draw()
# v_3 = sd.get_vector(start_point=v_2.end_point, angle=135, length=200, width=4)
# v_3.draw()
# v_4 = sd.get_vector(start_point=v_3.end_point, angle=180, length=200, width=4)
# v_4.draw()
# v_5 = sd.get_vector(start_point=v_4.end_point, angle=225, length=200, width=4)
# v_5.draw()
# v_6 = sd.get_vector(start_point=v_5.end_point, angle=315, length=200, width=4)
# v_6.draw()
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point

def figure()


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_RED, width=1)
        point = end_point


start_point = [(100, 100, 150, 3), (350, 100, 150, 4), (100, 350, 100, 5), (350, 350, 100, 6)]

for X in start_point:
    point_start = sd.get_point(X[0], X[1])
    length_start = X[2]
    heads_start = X[3]
    polygon(point_start, heads_start, length_start)

sd.pause()
