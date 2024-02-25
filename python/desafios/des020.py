# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

import random

nome1 = input('Nome 1° aluno:')
nome2 = input('Nome 2° aluno:')
nome3 = input('Nome 3° aluno:')
nome4 = input('Nome 4° aluno:')


print("A ordem de apresentação ficou: " ,random.sample([nome1,nome2,nome3,nome4], k=4))