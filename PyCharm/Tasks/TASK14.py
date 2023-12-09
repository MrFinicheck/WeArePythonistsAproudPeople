#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Возвращаем строку.
def get_input():
    line = input("Введите любую строку: ")
    return line


# Проверяем является ли значение числом.
def test_input(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False


# Преобразовываем переданное значение к целочисленному типу.
def str_to_int(number):
    string_number = int(number)
    return string_number


# Выводим переданное значение на экран.
def print_int(value):
    print(value)


if __name__ == '__main__':
    data = get_input()

    if test_input(data):
        return_value = str_to_int(data)
        print_int(return_value)
    else:
        print("Эта строка не является числом.")




