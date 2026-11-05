jogadores = list()
gols = list()
dic = dict()

while True:
    dic['nome'] = str(input('Qual o nome do jogador? '))
    dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou? '))

    for i in range(dic['partidas']):
        gols.append(int(input(f'Quantos gols o jogador fez na partida {i+1}? ')))
    dic['gols'] = gols[:]
    gols.clear()
    dic['aproveitamento'] = sum(dic['gols'])
    jogadores.append(dic.copy())
    dic.clear()

    r = input('Você quer adicionar mais jogadores? [S/N] ')
    if r in 'Nn':
        print('='*30)
        print('cod_nome')
        print('nome', 'gols', 'total')
        print('='*30)
        print('-'*30)
        
        for i, j in enumerate(jogadores):
            print(f'{i}  {j["nome"]}  {j["gols"]}  {j["aproveitamento"]}')
        
        print('='*30)

        while True:
            c = int(input('Mostrar dados de qual jogador? (999 encerra a busca) '))
            if c == 999:
                print('Programa encerrado!')
                break
            else:
                print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[c]["nome"]}:')
                for i, g in enumerate(jogadores[c]['gols']):
                    print(f'   No jogo {i+1} fez {g} gols.')
                print(f'  {jogadores[c]["nome"]} teve um aproveitamento de {jogadores[c]["aproveitamento"]} por partida.')
        break
