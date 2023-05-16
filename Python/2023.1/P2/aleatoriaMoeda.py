import random

semente = random.seed(int(input()))
jogadas = 100

cara = 'Ca'
coroa = 'Co'
moeda = [cara, coroa]
resultado = ''

premios = []
jogada = 0

while jogada <= jogadas:
    # Gere o numero n da jogada na qual a primeira cara aparece
    # Jogue a moeda
    n = random.choice(moeda)
    #print(n)
    # Se a moeda for cara, calcule o premio final:
    if n == cara:
        n = jogada + 1
        premio = 2 * n
        premios.append(premio)
        # finalize o loop: jogada = 101
    # Se for coroa, agregue a jogada ao resultado final
    else:
        resultado += n
        # 991
        # print(resultado)
        # finalize o loop: jogada = 101
    jogada += 1

media = sum(premios)/100
print(media)
