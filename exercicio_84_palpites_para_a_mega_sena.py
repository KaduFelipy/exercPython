from random import randint
lista_jogos = list()
jogos = list()
n_jogos = int(input('Digite o numero de jogos que será gerado'))

for i in range (n_jogos):
    for j in range (6):
        numero_gerado = randint(0,60)
        jogos.append(numero_gerado)
    lista_jogos.append(jogos[:])
    jogos.clear()

for i in range (len(lista_jogos)):
    print(f'{lista_jogos[i]}\n')
