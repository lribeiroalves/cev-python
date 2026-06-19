# Exercicio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valor = float(input('Digite um valor em metros: '))

print(f'A medida de {valor}m corresponde a')
print(f'{valor / 1000}km')
print(f'{valor / 100}hm')
print(f'{valor / 10}dam')
print(f'{valor * 10}dm')
print(f'{valor * 100}cm')
print(f'{valor * 1000}mm')
