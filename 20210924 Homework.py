#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:20:40 2021

@author: giotseng
"""


math = input('請輸入數學成績 : ')
engilsh = input('請輸入你的英文成績 : ') 
math = int(math)
engilsh = int(engilsh) 


if (math >= 90 and engilsh >= 90 ):
    print('太棒了!有獎勵!')   
elif (math < 60 and engilsh < 60):
    print('你完蛋了!!!')
elif (math < 60 or engilsh < 60):
    print('再加油!!!')
else : 
    print('ok!!!')

            
                                                                                  