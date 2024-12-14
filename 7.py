# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:32:40 2024

@author: vaip8
"""

import requests

def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")