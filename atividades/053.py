# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:35:19 2021

@author: lipy_
"""

frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')