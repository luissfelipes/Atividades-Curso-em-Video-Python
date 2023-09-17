# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:16:31 2021

@author: lipy_
"""

n = float(input('Insira quantos reais você tem: '))

d = n / 3.27

if d == 1:
    print('Voce possui US${:.2f} dolar. '.format(d))
if d < 1:
    print('Voce possui US${:.2f} centavos de dolar.'.format(d))
if d > 1:
    print('Voce tem US${:.2f} dolares.'.format(d))
