#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geom(*nums):
    multi = 1
    for i in nums:
        multi *= i
    sr_geom = pow(multi, 1/len(nums))
    return sr_geom


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    if not list_n:
        print("None")
    else:
        print(geom(*list_n))