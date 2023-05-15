# Regra do programa: Este programa recebe uma quantidade tam de numeros inteiros e retorna as posições do maior e do menor inteiro dessa lista, bem como seus valores e a variação entre eles..
# Exceções: Caso haja mais de um máximo ou minimo, o programa deve retornar o menor indice dos máximos/mínimo da lista.

# Passo 1: Leia a lista de números
lista = list(map(int, input().split()))
# Passo 2: Faça a mágica
max = max(lista) # Retira o maior valor
min = min(lista) # Retira o menor valor
# Passo 2.1: Calcule a variação entre o máximo e o mínimo
var = max - min
# Passo 3: Imprima a posição do máximo, o valor do máximo, a posição do mínimo, o valor do mínimo e a variação entre o máximo e o mínimo.
print('{} {} {} {} {}'.format(lista.index(max), max, lista.index(min), min, var))