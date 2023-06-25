# -*- coding: utf-8 -*-
# Programa dicionarios05.py
# Programador:
# Data: 21/06/23

# A avaliação da disciplina de Algoritmos e Programação I
# é composta de três provas e dois trabalhos. Projete um
# programa que leia um conjunto de alunos com as respectivas notas
# das provas e dos trabalhos. O programa deve ordenar os alunos pelo
# primeiro nome usando o método de ordenação por inserção
# (insertionSort). O programa deve imprimir a lista dos alunos ordenada
# pelo primeiro nome.

# início do módulo principal


# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho do conjunto de conjunto de teste
tam = int(input())
# Passo 1.2. Leia os dados dos estudantes
chaves = ['nome', 'snome', 'notas']
estudante = [dict.fromkeys(chaves) for _ in range(tam)]
dados = []
for i in range(tam):
    # Leitura
    dados = input().split()
    # Atribuição
    estudante[i]['nome'] = dados[0]
    estudante[i]['snome'] = dados[1]
    estudante[i]['notas'] = list(map(float, dados[2].split()))

    # Média final do aluno
    # 1. Media provas
    mediaprovas = sum(estudante['notas'][:3]) / 3.0
    # 2. Media trabalho
    mediatrab = sum(estudante['notas'][3:]) / 2.0
    # 3. Media final
    mediafinal = 0.75 * mediaprovas + 0.25 * mediatrab

print(estudante)
# Passo 2.2 Ordene os dados

# Passo 2.1.1. Atribua a temp o valor a ser inserido na lista ordenada

# Passo 3. Imprima os Dados
#for i in range(tam):
 #   print('{0:s} {1:s} {2:.1f}'.format(estudante[i]['nome'], estudante[i]['snome'],
#   estudante[i]['mf']))
# fim do módulo principal
