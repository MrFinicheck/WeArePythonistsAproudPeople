#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys


def get_person():
    """
    Запросить данные о личносте.
    """
    # Запросить данные о личности.
    name = input("Фамилия и имя? ")
    zodiac_sign = input("Знак Зодиака? ")
    birth_date = input("Дата рождения? ")

    # Создать словарь.
    return {
        'name': name,
        'zodiac_sign': zodiac_sign,
        'birth_date': birth_date
    }


def display_persons(staff):
    """
    Отобразить список линостей.
    """
    # Проверить, что список личностей не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех личностях.
        for idx, person in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    person.get('name', ''),
                    person.get('zodiac_sign', ''),
                    person.get('birth_date', 0)
                )
            )
        print(line)

    else:
        print("Список личностей пуст.")


def select_persons(staff, period):
    """
    Выбрать личностей с заданным месяцем.
    """
    # Инициализировать счетчик.
    count = 0

    # Сформировать список личностей.
    result = []

    # Проверить сведения личностей из списка.
    for person in staff:
        if period == int(person.get("birth_date").split('.')[1]):
            result.append(person)

    # Возвратить список выбранных личностей.
    return result

def main():
    """
    Главная функция программы.
    """
    # Список личностей.
    persons = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command:
            case 'exit':
                break

            case 'add':
                # Запросить данные о работнике.

                person = get_person()

                # Добавить словарь в список.
                persons.append(person)

                # Отсортировать список в случае необходимости.
                if len(persons) > 1:
                    persons.sort(key=lambda item: item.get('zodiac_sign', ''))

            case 'list':
                # Отобразить всех личностей.
                display_persons(persons)

            case 'select':
                # Разбить команду на части для выделения месяца.
                parts = command.split(' ', maxsplit=1)

                # Получить требуемый месяц.
                month = int(parts[1])

                # Выбрать личностей с заданным месяцем.
                selected = select_persons(persons, month)

                # Отобразить выбранных личностей.
                display_persons(selected)

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить личность;")
                print("list - вывести список личностей;")
                print("select <месяц> - запросить личностей с этим месяцем;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
