tam = int(input())
lista = list(map(int, input(). split()))

msg = 'verdadeiro'
i = 0
while i < tam-1:
#for i in range(tam-1):
    if lista[0] <= lista[i+1]:
        msg = 'falso'
        i = tam
    i += 1

print(msg)