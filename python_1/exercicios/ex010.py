# Exercicio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considere US$1.00 = R$3.27

dinheiro = float(input('Quanto dinheiro voce tem na carteira? R$'))

print(f'Com R${dinheiro:.2f}, voce pode comprar US${dinheiro / 3.27:.2f}.')
