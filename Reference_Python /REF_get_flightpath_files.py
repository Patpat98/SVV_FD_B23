#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:57:11 2019

@author: edmundo
"""

from bs4 import BeautifulSoup
import urllib.request
import requests
#import os

r  = requests.get("http://dueca.tudelft.nl/testflight/data_2019/MAT/")
data = r.text
soup = BeautifulSoup(data)

files = []

for link in soup.find_all('a'):
    files.append(link.get('href'))
    
wrong_files = []

for i in range(len(files)):
    file = files[i]
    if file[-3:] != 'mat':
        wrong_files.append(files[i])
        
correct = [x for x in files if x not in wrong_files]
    

print(correct)
print(len(correct))

for j in range(len(correct)):
    link = "http://dueca.tudelft.nl/testflight/data_2019/MAT/" + correct[j]
    urllib.request.urlretrieve(link, correct[j])
