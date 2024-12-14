# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:32:47 2024

@author: vaip8
"""

import re

def extract_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return re.findall(r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}', content)