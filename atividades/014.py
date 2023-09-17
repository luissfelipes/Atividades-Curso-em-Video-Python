# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:27:35 2021

@author: lipy_
"""

t = float(input('Digite a temperatura em graus Celsius: '))

t2 = 1.8 * t + 32

print('{:.2f} graus Celsius equivalem a {:.2f} graus Fahrenheit.'.format(t, t2))