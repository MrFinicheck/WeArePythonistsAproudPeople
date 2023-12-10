#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    # Ввести целое число.
    number = int(input("Введите целое число: "))

    # Определить знак числа.
    if number > 0:
        positive()
    elif number < 0:
        negative()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == '__main__':
    test()




