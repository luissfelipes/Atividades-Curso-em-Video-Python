# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:46:08 2021

@author: lipy_
"""

p1 = float(input('Insira o valor original: '))

p2 = p1 * 0.05

p3 = p1 - p2

print()

print('O valor com 5% de desconto é: R${:.2f}'.format(p3))