# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex.: Digite um número(6.127). O número 6.127 tem a parte inteira 6.

from math import trunc


num = float(input('Digite um número decimal'))

print(f'The integer part of this number is {trunc(num)}')