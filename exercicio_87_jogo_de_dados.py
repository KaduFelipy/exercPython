from random import randint
from time import sleep

j = dict()
results = list()

for i in range (1):
    j['jogador1'] = randint(1,6)
    j['jogador2'] = randint(1,6)
    j['jogador3'] = randint(1,6)
    j['jogador4'] = randint(1,6)
    results.append(j.copy())
    j.clear()

ranking = sorted(results[0].items(), key=lambda item: item[1], reverse=True)
print('-'*30)
for pos, item in enumerate(ranking, start=1):
    print(f'{pos}º lugar: {item[0]} tirou {item[1]}')
    sleep(1)
