#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sr_garmon(*args):
    if not args:
        return None

    summa = 0
    d = len(args)
    for i in args:
        summa += 1/i
    x = d/summa
    return float(x)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    print(sr_garmon(*list_n))
