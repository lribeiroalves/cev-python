# Exercicio 011
# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m**2

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2

print(f'Sua parede mede {largura}*{altura}. A area da parede é de {area:.3f}m2')
print(f'Para pintar essa parede, voce precisará de: {tinta:.4f}l de tinta.')