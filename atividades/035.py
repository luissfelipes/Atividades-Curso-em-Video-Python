# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:32:49 2021

@author: lipy_
"""

a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))

n1 = b - c
n2 = a - c
n3 = a - b

p1 = b + c
p2 = a + c
p3 = a + b

if n1 < a < p1 and n2 < b < p2 and n3 < c < p3:
    print('É possivel formar um triângulo!')
else:
    print('Não é possivel')