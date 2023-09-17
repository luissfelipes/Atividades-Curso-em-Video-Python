# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:37:32 2021

@author: lipy_
"""

s = float(input('Digite seu salário atual: '))

s1 = (s * 0.10) + s

s2 = (s * 0.15) + s

if s > 1250:
    print(f'Seu novo salário será R${s1:.2f}.')
else:
    print(f'Seu novo salário será R${s2:.2f}.')
print()
print('Fim')