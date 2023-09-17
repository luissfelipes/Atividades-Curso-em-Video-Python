# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:04:38 2021

@author: lipy_
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Você foi reprovado.')
elif m >= 7:
    print('Você está foi aprovado.')
else:
    print('Você está em recuperação.')
    