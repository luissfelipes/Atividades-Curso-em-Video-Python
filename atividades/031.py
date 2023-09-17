# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:39:37 2021

@author: lipy_
"""

d = float(input('Qual a distancia da viagem em KM: '))

p1 = d * 0.50
p2 = d * 0.45

if d <= 200:
    print(f'O valor da viagem será R${p1:.2f}.')
else:
    print(f'O valor da viagem será R${p2:.2f}.')