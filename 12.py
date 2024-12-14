# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:33:19 2024

@author: vaip8
"""

from bs4 import BeautifulSoup
import requests

def scrape_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [headline.text for headline in soup.find_all('h1')]
    for i, headline in enumerate(headlines, start=1):
        print(f"{i}. {headline}")