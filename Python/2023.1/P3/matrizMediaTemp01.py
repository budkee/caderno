# inicialize a tabela de temperatura
temp = [ [0.0]*3 for i in range(4)]
# Leitura das temperaturas nos 3 locais
for i in range(0,4):
    print(f'Hora {i}')
    temp[i] = list(map(float, input().split()))
print(temp)

# Inicialize a lista de médias
mediaTemp = [0]*3
print(mediaTemp)

# Some as temperaturas de cada local
for i in range(0,3): # Para cada local
    soma = []
    r = 0
    for j in range(0,4):    # Some a temperatura de cada horário
        r += temp[i][j]
        soma.append(r)
    print(soma)
    mediaTemp[i] = soma[i]/4
    #print(mediaTemp)
# Imprima o resultado
for i in range(0,3): # Coluna
    print(i, mediaTemp[i])
