dicionario = dict()
def notas (*n, sit=False):
    listaNotas = n
    dicionario['total'] = len(listaNotas)
    dicionario['maior'] = max(listaNotas)
    dicionario['menor'] = min(listaNotas)
    dicionario['media'] = sum(listaNotas) / len(listaNotas)

    if sit:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'BOA'
        elif dicionario['media'] >= 5 and dicionario['media'] < 7:
            dicionario['situacao'] = 'RAZOAVEL'
        elif dicionario['media'] < 5:
            dicionario['situacao'] = 'RUIM'
        else:
            print('Algo de errado não está certo')

    print(dicionario)

notas(5,5.5,7,9, sit = True)
