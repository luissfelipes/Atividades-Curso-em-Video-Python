# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:41:27 2021

@author: lipy_
"""

import random

a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')

lista = a1, a2, a3, a4

nome = random.choice(lista)

print('O nome escolhido foi {}.'.format(nome))