# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:47:15 2021

@author: lipy_
"""

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print()
if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
