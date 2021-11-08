#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sr_garmon(*nums):
    summa = 0
    d = len(nums)
    for i in nums:
        summa += 1/i
    x = d/summa
    return float(x)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    if not list_n:
        print("None")
    else:
        print(sr_garmon(*list_n))
