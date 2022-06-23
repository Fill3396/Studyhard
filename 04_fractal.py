# -*- coding: utf-8 -*-
import random
import random as ra
import simple_draw as sd
sd.resolution = 1000, 600
point_0 = sd.get_point(500, 30)
random_lenght_gl = [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
COLOR_DARK_GREEN = (0, 127, 0)
def draw_branches(point, angle, length):
    if length < 3:
        return
    v_1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1,)
    v_1.draw()
    line_1 = sd.line(start_point=point, end_point=v_1.end_point, color=COLOR_DARK_GREEN, width=1)
    next_point = v_1.end_point
    random_angle = ra.randint(15, 45)
    next_angle = angle - random_angle
    random_lenght = random.choice(random_lenght_gl)
    next_length = length * random_lenght
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    random_angle_2 = ra.randint(15, 45)
    next_angle_2 = angle + random_angle_2
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)

draw = draw_branches(point=point_0, angle=90, length=150)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


