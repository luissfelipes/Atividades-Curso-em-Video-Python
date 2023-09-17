# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:03:02 2021

@author: lipy_
"""

import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('Suas opções')
print('-=' * 6)
print('0 - Pedra \n1 - Papel \n2 - Tesoura')
print('-=' * 6)
jogador = int(input('Faça sua jogada: '))
print()
print('-=' * 14)
print(f'Você escolheu {itens[jogador]}.')
print(f'O computador escolheu {itens[computador]}.')
print('-=' * 14)

if computador == 0:   #pedra
    if jogador == 0:
        resultado = ('Empate')
    elif jogador == 1:
        resultado = ('Você ganhou')
    elif jogador == 2:
        resultado = ('Você perdeu')
elif computador == 1:  #papel
    if jogador == 0:
        resultado = ('Você perdeu')
    elif jogador == 1:
        resultado = ('Empate')
    elif jogador == 2:
        resultado = ('Você ganhou')
elif computador == 2:  # tesoura
    if jogador == 0:
        resultado = ('Você ganhou')
    elif jogador == 1:
        resultado = ('Você perdeu')
    elif jogador == 2:
        resultado = ('Empate')
else:
    resultado = ('Valor invalido')
 
print('Jo')
time.sleep(0.5)
print('ken') 
time.sleep(0.5) 
print('po!')
time.sleep(0.5)
print(resultado)