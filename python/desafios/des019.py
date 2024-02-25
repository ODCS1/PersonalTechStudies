# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele. Lendo o nome deles e escrevendo o nome escolhido.

import random

nome1 = input('Nome 1° aluno:')
nome2 = input('Nome 2° aluno:')
nome3 = input('Nome 3° aluno:')
nome4 = input('Nome 4° aluno:')

lista = [nome1, nome2, nome3, nome4]

print(random.choice(lista))

print(type(lista))


