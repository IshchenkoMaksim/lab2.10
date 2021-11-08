#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sr_geometr(*nums):
    if not nums:
        return None

    multi = 1
    for i in nums:
        multi *= i
    sr_geom = pow(multi, 1/len(nums))
    return float(sr_geom)


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    print(sr_geometr(*list_n))
