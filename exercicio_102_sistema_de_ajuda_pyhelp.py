from time import sleep

while True:

    print('\033[93m-\033[0m*30)
    print('\033[93mSISTEMA DE AJUDA PyHELP\033[0m'.center(30))
    print('\033[93m-\033[0m*30)

    r = str(input('Função ou Biblioteca -> '))

    if r == 'fim':
        print('\033[31m-\033[0m30)
        print(f'\033[31mATÉ LOGO!\033[0m'.center(30))
        print('\033[31m-\033[0m30')
        break

    else:

        sleep(2)

        print('\033[93m-\033[0m*30)
        print(f'\033[94mAcessando o manual do comando "{r}"\033[0m'.center(30))
        print('\033[93m-\033[0m*30)

        sleep(2)

        print('\033[96m-\033[0m*30)
        print(f'\033[96m{help(r)}\033[0m'.center(30))
        print('\033[96m-\033[0m*30)

        sleep(1)
