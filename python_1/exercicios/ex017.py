# Exercicio 017
# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math

cat_opo = float(input('Digite o valor do Cateto Oposto:'))
cat_adj = float(input('Digite o valor do Cateto Adjacente: '))

print(f'A hipotenusa de um triangulo retangulo com catetos Oposto={cat_opo} e Adjacente={cat_adj} é igual a {math.hypot(cat_opo, cat_adj)}')