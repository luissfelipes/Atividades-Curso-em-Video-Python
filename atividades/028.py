# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:03:49 2021

@author: lipy_
"""
import random
import time
n = int(input('Digite um numero de 0 a 5: '))

a1 = 0
a2 = 1
a3 = 2
a4 = 3
a5 = 4
a6 = 5

lista = (a1, a2, a3, a4, a5, a6)

num = random.choice(lista)

print('Carregando')
time.sleep(1.5)

if n == num:
    print('Parabéns, voce acertou!')
else:
    print('Você errou.')
    