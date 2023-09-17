# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:16:55 2021

@author: lipy_
"""

n = int(input('Digite um numero inteiro: '))
print()
print('''Escolha uma das bases para fazer a conversão: 

1 - Converter para Binário
2 - Converter para Octal
3 - Converter para Hexadecimal''')
      
escolha = int(input('Escolha uma: '))

if escolha == 1:
    print(f'{n} convertido para Binário é igual a {bin(n)[2:]}.')
elif escolha == 2:
    print(f'{n} convertido para Octal é igual a {oct(n)[2:]}.')
elif escolha == 3:
    print(f'{n} conertido para Hexadecimal é igual a {hex(n)[2:]}.')
else:
    print('Valor inválido.')