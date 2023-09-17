# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:55:29 2021

@author: lipy_
"""

num = int(input('Digite um numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')   
print(f'\n\033[0mO numero {num} foi divisivel  {tot}.')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('Por isso ele não é primo.')
        