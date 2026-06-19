# Exercicio 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a1 = input('Digite o nome do 1º Aluno: ')
a2 = input('Digite o nome do 2º Aluno: ')
a3 = input('Digite o nome do 3º Aluno: ')
a4 = input('Digite o nome do 4º Aluno: ')

aluno = random.choice((a1, a2, a3, a4))

print(f'O aluno(a) escolhido(a) foi {aluno}')