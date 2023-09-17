# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:46:06 2021

@author: lipy_
"""
import datetime
a = int(input('Digite um ano: '))

c1 = a % 4 
c2 = a % 100
c3 = a % 400

if a == 0:
    a = datetime.date.today().year
if c1 == 0 and c2 != 0 or c3 == 0:
    print('é bi')
else:
    print('nao')
print()
print('Fim')                