#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sr_geometr(*args):
    if not args:
        return None

    multi = 1
    for i in args:
        multi *= i
    sr_geom = pow(multi, 1/len(args))
    return float(sr_geom)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    print(sr_geometr(*list_n))
