# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:55:05 2021

@author: lipy_
"""


import datetime

a = int(input('Digite seu ano de nascimento: '))

idade = datetime.date.today().year - a

tr = 18 - idade

if tr == 0:
    print('Esta na hora de se alistar!')
elif tr > 1:
    print('Ainda não está na hora de se alistar.')
    print(f'Tempo restante: {18 - idade} anos.')
elif tr == 1:
    print('Ainda não esta na hora de se alistar.')
    print(f'Tempo restante: {tr} ano.')
else:
    print('Já passou da data de alistamento.')
    print(f'Você está {idade - 18} anos atrasado.')




