# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:32:44 2021

@author: lipy_
"""

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))


if n1 < n2 and n3:
    menor = n1
if n2 < n1 and n3:
    menor = n2
if n3 < n1 and n2:
    menor = n3
if n1 > n2 and n3:
    maior = n1
if n2 > n1 and n3:
    maior = n2
if n3 > n2 and n1:
    maior = n3
print(f'O menor número digitado foi: {menor}. \nO maior número digitado foi: {maior}.')