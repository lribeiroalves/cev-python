# Exercicio 020
# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = input('Digite o nome do 1º Aluno: ')
a2 = input('Digite o nome do 2º Aluno: ')
a3 = input('Digite o nome do 3º Aluno: ')
a4 = input('Digite o nome do 4º Aluno: ')

alunos = random.sample((a1, a2, a3, a4), k=4,)
print('A ordem de apresentação será:')
for i in range(4):
    print(f'{i+1}º Aluno: {alunos[i]}')