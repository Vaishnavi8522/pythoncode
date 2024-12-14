# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:29 2024

@author: vaip8
"""

def word_frequency(paragraph):
    words = paragraph.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency