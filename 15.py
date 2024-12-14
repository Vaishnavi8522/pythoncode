# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:34 2024

@author: vaip8
"""

def optimized_code(numbers):
    result = ""
    even_squares = {num: num * num for num in numbers if num % 2 == 0}
    for num, square in even_squares.items():
        result += f"Square of {num} is {square}\n"

    max_num = max(numbers)
    count_dict = {num: numbers.count(num) for num in set(numbers)}

    result += f"\nMax number is {max_num}\n"
    result += "Number counts:\n"
    for num, count in count_dict.items():
        result += f"{num}: {count}\n"

    return result