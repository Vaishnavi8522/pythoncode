# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:30:11 2024

@author: vaip8
"""

def second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second