# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:14:33 2021

@author: lipy_
"""

import math

n = float(input('Digite o valor do angulo: '))

cos = math.cos(math.radians(n))
sen = math.sin(math.radians(n))
tan = math.tan(math.radians(n))

print('O seno de {} graus é {}. \nO coseno de {} graus é {}. \nA tangente de {} graus é {}'.format(n, sen, n, cos, n, tan))
              