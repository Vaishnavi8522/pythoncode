# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:13 2024

@author: vaip8
"""

import json

def parse_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    for key, value in data.items():
        print(f"{key}: {value}")