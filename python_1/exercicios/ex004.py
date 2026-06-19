# Exercicio 004
# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

ans = input('Digite algo: ')

print(f'Voce digitou: {ans}')
print(f'"{ans}" e do tipo: {type(ans)}')
print(f'"{ans}" e numerico: {ans.isnumeric()}')
print(f'"{ans}" e alfabetico: {ans.isalpha()}')
print(f'"{ans}" e alfanumerico: {ans.isalnum()}')
print(f'"{ans}" e minusculo: {ans.islower()}')
print(f'"{ans}" e maiusculo: {ans.isupper()}')
print(f'"{ans}" e capitalizado: {ans.istitle()}')
print(f'"{ans}" e espaco: {ans.isspace()}')
print(f'"{ans}" e imprimivel (caractereres que podem ser impressos): {ans.isprintable()}')
print(f'"{ans}" e ascii: {ans.isascii()}')
print(f'"{ans}" e decimal: {ans.isdecimal()}')
print(f'"{ans}" e digito: {ans.isdigit()}')
print(f'"{ans}" e pode ser um identifier: {ans.isidentifier()}')