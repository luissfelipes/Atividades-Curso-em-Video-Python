# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:28:47 2021

@author: lipy_
"""

import math

a = float(input('Digite o cateto oposto: '))
o = float(input('Digite o cateto adjacente: '))
       
h = math.hypot(a, o)
print()
print('O valor da hipotenusa é: {:.2f}.'.format(h))
