dic = dict()
gols = list()
dic['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for i in range(total_partidas):
    gols.append(int(input(f'Quantos gols o jogador fez na partida {i+1}? ')))
dic['gols'] = gols
dic['total'] = sum(gols)
print('='*30)
print(dic)
print('='*30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print('='*30)
for i, v in enumerate(dic['gols']):
    print(f'--> Na partida {i+1}, fez {v} gols')
