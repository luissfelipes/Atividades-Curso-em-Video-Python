# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:31:34 2021

@author: lipy_
"""

a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))

n1 = b - c
n2 = a - c
n3 = a - b

p1 = b + c
p2 = a + c
p3 = a + b

print()

if n1 < a < p1 and n2 < b < p2 and n3 < c < p3:
    print('É possivel formar um triângulo!')
    print()
    if a == b == c:
        print('Este triangulo é Equilátero.')
    elif a == b or a == c or b == a:
        print('Este triângulo é Isósceles.')
    else:
        print('Este triângulo é Escaleno.')
else:
    print('Não é possivel')