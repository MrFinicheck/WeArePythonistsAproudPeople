#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    product = 1
    number = int(input("Введите число: "))

    while number != 0:
        product *= number
        number = int(input("Введите число: "))

    print(product)


if __name__ == '__main__':
    multiply()





