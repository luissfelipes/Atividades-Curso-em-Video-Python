# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:34:51 2021

@author: lipy_
"""

h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
print()

a = h * l 

t = a / 2
print('A area tem o valor de {:.3f}m².'.format(a))
print()
print('Serão necessários {:.3f} litros de tinta.'.format(t))