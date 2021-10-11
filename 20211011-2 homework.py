#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:19:36 2021

@author: giotseng
"""

import random
ans = random.randint(1, 20)
counter = 0

while counter < 5 :
    guess = int(input('請猜1-20間的一個數字！'))
    if guess > ans :
        print('小一點')
        counter = counter + 1
        i = 5 - counter
        i = str(i)
        print('還剩下'+i+'次')
    elif guess < ans :
        print('大一點')
        counter = counter + 1
        i = 5 - counter
        i = str(i)
        print('還剩下'+i+'次')
    else:
        print('恭喜你答對了!')
        
        break
