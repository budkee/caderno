# Passo 1. Leia quatro palavras
pal1, pal2, pal3, pal4 = map(str, input().split())
# Passo 2. Retirar a primeira letra de cada item da lista e colocar na listaF
lista = [pal1, pal2, pal3, pal4]
listaF = []
for l in range(len(lista)):
    listaC = lista[l]
    listaT = listaC[0]
    listaF.append(listaT)
# Passo 2.1. Verifique se os caracteres estão em ordem
if (ord(listaF[0]) < ord(listaF[1])) and (ord(listaF[1]) < ord(listaF[2])) and (ord(listaF[2]) < ord(listaF[3])):
    msg = 'ordem crescente'
else:
    msg = 'não estão em ordem crescente'

print('{0:s}'.format(msg))