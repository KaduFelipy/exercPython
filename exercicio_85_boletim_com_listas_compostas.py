lista = list()
dados = list()

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite a primeira nota: ')))
    dados.append(int(input('Digite a segunda nota: ')))
    lista.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'NN':
        print('No.  NOME   Média')
        for pos,i in enumerate(lista):
            print(f'{pos + 1}    {i[0]}    {(i[1] + i[2])/2}')
        while True:
            n = int(input('Mostrar as notas de qual aluno? (999 interrompe)'))
            if n == 999:
                print('Você finalizou o programa!')
                break
            else:
                print(f'As notas de {lista[n -1][0]} são [{lista[n -1][1]},{lista[n-1][2]}]')
        break
