# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:54:21 2021

@author: lipy_
"""

a1 = int(input('Digite o primeiro termo da sequência: '))
r = int(input('Digite a razão: '))

print ()

for c in range(0, 10):
    print(f'{a1 + c * r} => ', end=' ',)
print('acabou')
    
    