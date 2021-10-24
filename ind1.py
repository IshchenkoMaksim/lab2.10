#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Произведение аргументов, расположенных
# между первым и вторым нулевыми аргументами.


def multi_between_0(*nums):
    multi = 1
    count = 0
    for idx, n in enumerate(nums):
        if n == 0:
            nums = nums[idx+1:]
            count += 1
            break
    for idx, n in enumerate(nums):
        if n == 0:
            nums = nums[:idx]
            count += 1
            break
    if count != 2:
        return "Недостаточно нулей"
    else:
        for n in nums:
            multi *= n
        return multi


if __name__ == '__main__':
    list_n = list(map(float, input("Введите числа через пробел: ").split()))
    if not list_n:
        print("None")
    else:
        print(multi_between_0(*list_n))
