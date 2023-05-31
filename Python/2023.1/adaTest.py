lista = [55, 16, 37, 23, 68, 97, 69, 85, 10, 15]
a = []
b = []

for i in range(len(lista)):
    if i%2 == 0:
        a.append(lista[i])
    else:
        b.append(lista[i])
print(a, b)