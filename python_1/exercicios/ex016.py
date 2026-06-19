# Exercicio 016
# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite o número 6.127. O numero tem a parte inteira 6

import math

num = float(input('Digite um numero real: '))
print(f'A parte inteira do numero {num} é {math.trunc(num)}.')