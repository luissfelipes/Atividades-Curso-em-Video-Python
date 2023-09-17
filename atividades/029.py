# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:22:59 2021

@author: lipy_
"""

v = float(input('Digite a velocidade do carro: '))

m = (v - 80) * 7

if v > 80:
    print('Você ultrapassou o limite de velocidade.')
    print(f'Sua multa será de R${m:.2f}.')
else:
    print('Siga com segurança.')