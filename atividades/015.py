# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:47:20 2021

@author: lipy_
"""

n1 = float(input('Qual a quantidade de Km rodados: '))

n2 = int(input('Quantos dias o carro foi alugado: '))
         
p = (0.15 * n1) + (60 * n2)

print()

print('O total a ser pago é R${:.2f}.'.format(p))

