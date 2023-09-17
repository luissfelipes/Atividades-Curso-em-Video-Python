# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:33:18 2021

@author: lipy_
"""
cont = 0
s = 0
for n in range(1, 501):
    if n % 3 == 0:
        numero = n
        if numero % 2 != 0:
            numero = n
            s = s + n
            cont = cont + 1
print(f'A soma de {cont} valores é {s}.')