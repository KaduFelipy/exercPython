from time import sleep

def contagem (inicio, final, passo):
    if passo == 0:
        print('O passo não pode ser zero')
        return

    if inicio > final and passo > 0:
        final = final -1
        passo = -passo

    elif inicio < final and passo < 0:
        final = final + 1
        passo = -passo

    for i in range( inicio, final, passo):
        print(i, end=' ')
        sleep(1)
    print('FIM!')

while True:
    contagem(0,10,1)

    contagem(10,0,2)

    print('Agora é sua vez de personalizar a contagem!')

    inicio = int(input('Qual será o início da contagem? '))
    final = int(input('Qual será o final da contagem? '))
    passo = int(input('Qual será o passo da contagem? '))

    print('-='*30)

    contagem(inicio, final, passo)

    print('-='*30)

    r = input('Deseja fazer mais uma personalização? [S/N]')

    if r in 'nN':
        print('Programa encerrado! \n Até mais!')
        break
