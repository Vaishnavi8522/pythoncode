# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:26:39 2024

@author: vaip8
"""

def sum_integers_from_file(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total