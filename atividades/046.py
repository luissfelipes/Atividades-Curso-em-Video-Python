# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:55:56 2021

@author: lipy_
"""

from time import sleep

print('Contagem')

for c in range(10, -1, -1):
    print(f'Contagem regressiva: {c}')
    sleep(1)
print('Fim')