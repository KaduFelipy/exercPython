alunos = dict()
dados = {}
while True:
    print('='*30)
    dados['nome'] = str(input('Digite o nome do aluno: '))
    dados['media'] = float(input('Digite a media do aluno: '))
    if dados['media'] >= 7:
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'
    alunos.append(dados.copy())
    print('='*30)
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        for i in alunos:
            for k, v in i.items():
                print(f'{k} é igual a {v}')
        break
