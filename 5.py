# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:31:23 2024

@author: vaip8
"""

def validate_integer_input(user_input):
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a number.")