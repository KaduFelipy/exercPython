lista = list()
listaMulheres = list()
dados = dict()
idades = 0

while True:
    dados['nome'] = str(input('Qual o seu nome? '))
    dados['sexo'] = str(input('Qual o seu sexo? '))
    dados['idade'] = int(input('Qual a sua idade? '))
    lista.append(dados.copy())
    r = input('Você quer cadastrar mais pessoas? [S/N] ')
    r.lower()
    if r == 'n':
        if dados['sexo'] in 'Ff':
            listaMulheres.append(dados['nome'])
        
        for i in lista:
            idades = idades + i['idade']
        media = idades/len(lista)

        print(f'Foram cadastradas {len(lista)} pessoas')
        print(f'A média de idade do grupo é {media:.2f}')
        print(f'Lista de mulheres do grupo: {listaMulheres}')

        for i in lista:
            if i['idade'] > media:
                print(f'{i["nome"]} está acima da idade média do grupo')
        break
