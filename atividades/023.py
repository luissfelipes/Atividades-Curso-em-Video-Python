# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:55:38 2021

@author: lipy_
"""

nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(' '))
print(nome.find(' '))