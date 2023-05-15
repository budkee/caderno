# -*- coding: utf-8 -*-
# Programa: maiorpalavra01.py
# Programados:
# Data: 07/11/2016
# Este programa le três palavras, computa qual e a maior
# (lexicograficamente) e imprime a maior.
# início do módulo principal
# descrição das variáveis utilizadas
# string palavra1, palavra2, palavra3, maior

# pré: palavra1 palavra2 palavra3

# Passo 1. Leia as palavras
palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())
# Passo 2. Compute a maior palavra
if (palavra1 > palavra2) and (palavra1 > palavra3):
    maior = palavra1
elif (palavra2 > palavra3) and (palavra2 > palavra1):
    maior = palavra2
else: # (palavra3 > palavra1) and (palavra3 > palavra2):
    maior = palavra3
# Passo 3. Imprima a maior palavra
print('Maior palavra = {0:s}'.format(maior))

# pós: maior and maior == max{palavra1, palavra2, palavra3}
# fim do módulo principal