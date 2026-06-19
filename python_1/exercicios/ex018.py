# Exercicio 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.abs

import math

angulo = float(input('Digite o valor do angulo: '))
angulo_rad = math.radians(angulo)

print(f'O angulo {angulo} tem:')
print(f'Seno = {math.sin(angulo_rad):.3f}')
print(f'Cosseno = {math.cos(angulo_rad):.3f}')
print(f'Tangente = {math.tan(angulo_rad):.3f}')
