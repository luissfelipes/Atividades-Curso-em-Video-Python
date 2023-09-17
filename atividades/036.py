# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:31:29 2021

@author: lipy_
"""

c = float(input('Digite o valor da casa: '))
s = float(input('Digite seu salário: '))
a = int(input('Quantos anos vai ser paga a casa: '))
print()

m = a * 12

mp = s * 0.30

vp = c / m

if vp > mp:
    print('Empréstimo negado!')
else:
    print(f'Empréstimo aprovado! Sua casa no valor de {c:.2f}, será pago em {m} vezes, com parcelas de R${vp:.2f}.')