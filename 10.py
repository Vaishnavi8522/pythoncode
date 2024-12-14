# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:07 2024

@author: vaip8
"""

import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)