# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:30:45 2021

@author: lipy_
"""

import datetime



atual = datetime.date.today().year

for pessoas in range (1,8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        print('Essa pessoa é maior.')
    else:
        print('Essa pessoa é menor.')