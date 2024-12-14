# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:00 2024

@author: vaip8
"""

from statistics import mean, median, mode

def calculate_statistics(data):
    return {
        "Mean": mean(data),
        "Median": median(data),
        "Mode": mode(data)
    }