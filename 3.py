#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Написать функцию преворачивающую значения ключей
# (чтобы значения шли в обратном порядке)


def dict_reverse(**dict_f):
    keys = []
    for k in dict_f.keys():
        keys.append(k)

    values = []
    for v in dict_f.values():
        values.append(v)

    values.reverse()

    return dict(zip(keys, values))


if __name__ == '__main__':
    sl = dict()

    while True:
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        if key == '' or value == '':
            break
        sl.setdefault(key, value)

    sl = dict_reverse(**sl)

    for k, v in sl.items():
        print(k, 'is', v)
