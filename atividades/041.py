# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:12:24 2021

@author: lipy_
"""
from datetime import date

a = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - a

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')