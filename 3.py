#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать функцию преворачивающую значения ключей
# (чтобы значения шли в обратном порядке)


def reverse(**kwargs):
    keys = []
    [keys.append(k) for k in kwargs.keys()]

    values = []
    [values.append(v) for v in kwargs.values()]

    values.reverse()

    return dict(zip(keys, values))


if __name__ == '__main__':
    result = reverse(one=1, two=2, three=3, four=4, five=5)

    for key, value in result.items():
        print(key, '=', value)
