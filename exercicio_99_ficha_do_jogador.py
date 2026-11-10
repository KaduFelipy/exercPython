def ficha(nome = '', gols = 0):
    if nome == '':
        nome = '<Desconhecido>'

    print(f'O jogador {nome} fez {gols} gols no campeonato.')

nome = str(input('Nome do jogador: '))
gols = int(input('Numero de gols: '))

ficha(nome,gols)
