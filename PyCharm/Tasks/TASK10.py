#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    # Определить функцию для нахождения площади круга.
    def circle(radius):
        return math.pi * radius ** 2

    # Ввести радиус и высоту цилиндра.
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    # Посчитать площади боковой и всей поверхностей.
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = (lateral_surface_area +
                          2 * circle(radius))

    # Узнать хочет ли получить пользователь всю площадь.
    solution = input("Хотите получить только площадь не "
                     "только боковой поверхности, но и "
                     "цилиндра? (Да/Нет): ")

    if solution.lower() == "да":
        print(f"Площадь боковой поверхности цилиндра: "
              f"{lateral_surface_area}")
    else:
        print(f"Полная площадь цилиндра: "
              f"{total_surface_area}")


if __name__ == '__main__':
    cylinder()





    
