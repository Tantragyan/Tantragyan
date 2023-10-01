# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:17:43 2020

@author: vyomk
"""

for x in range(0, 1):
    print("Hello World")
    for x in range(0, 1):
        print("My name is Vyom")
year = input('Year of birth: ') 

if not bool(year.rstrip()): 
    print('You need to enter a value for your year of birth') 