# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 22:10:23 2021

@author: lipy_
"""

p = float(input('Insira seu peso em kg: '))
h = float(input('Insira sua altura em centimetros: '))

h2 = h / 100
imc = p / (h2 ** 2)

print()

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}, você está abaixo do peso.')
elif imc < 25:
    print(f'Seu imc é {imc:.1f}, voce está com peso ideal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.1f}, você está com sobrepeso.')
elif imc < 40:
    print(f'Seu IMC é {imc:.1f}, vocÊ está com obesidade.')
else:
    print(f'Seu IMC é {imc:.1f}, você está com obesidade mórbida.')