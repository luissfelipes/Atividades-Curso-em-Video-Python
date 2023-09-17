# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:34:25 2021

@author: lipy_
"""

print('=' * 20,'SUPERMERCADO AQUATON','=' *20)
print()


p = float(input('Digite o valor original do produto: '))
print()
print('Selecione a forma de pagamento: ')

print('1 - À vista dinheiro/cheque com 10% de desconto \n2 - À vista no cartão com 5% de desconto \n3 - Em 2x no cartão sem juros \n4 - 3x ou mais no cartão com 20% de desconto')
print()

forma = int(input('Digite a forma de pagamento escolhida: '))

if forma == 1:
    total = p - (p * 0.10)
elif forma == 2:
    total = p - (p * 0.05)
elif forma == 3:
    total = p
    print(f'Sua compra será em 2 vezes, com parcelas de R${total / 2:.2f}.')
elif forma == 4:
    total = p + (p * 0.20)
    parc = int(input('Qual será a quantidade de parcelas: '))
    totpar = total / parc
    print(f'Sua compra sera em {parc} vezes, com parcelas de R${totpar:.2f} por mês.')
print(f'Sua compra de R${p:.2f} vai custar R${total:.2f} no total.')