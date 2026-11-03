times_brasileirao = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Fluminense",
    "Athletico-PR",
    "Bahia",
    "Atlético-MG",
    "Red Bull Bragantino",
    "Santos",
    "São Paulo",
    "Coritiba",
    "Botafogo",
    "Vasco",
    "Vitória",
    "Grêmio",
    "Mirassol",
    "Corinthians",
    "Internacional",
    "Remo",
    "Chapecoense"
)

while True:
    print('\n')
    print('-'*30)
    print('Bem vindo a tabela do brasileirão!')
    print('-'*30)
    print('\n')
    print('[A] - Mostrar os 5 primeiros colocados')
    print('[B] - Mostrar os 4 últimos colocados')
    print('[C] - Mostrar tabela completa em ordem alfabética')
    print('[D] - Mostrar classificação da Chapecoense')
    print('\n')
    a = input('Selecione uma opção:').upper()
    match a:
        case 'A':
            for i in range (0,5):
                print('{}º - {}'.format(i,times_brasileirao[i]))
        case 'B':
            for i in range (len(times_brasileirao),len(times_brasileirao)-4,-1):
                print('{}º - {}'.format(i,times_brasileirao[i -1]))
        case 'C':
            for times in sorted(times_brasileirao):
                print(times)
        case 'D':
            posicao = times_brasileirao.index('Chapecoense')
            print(f'A chapecoense está em {posicao}º lugar.')
        case _:
            print('Seleção errada!')
            print('Programa encerrado!')
            break
