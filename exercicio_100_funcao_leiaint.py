def leiaint():
    while True:
        n = input('Digite um numero de 0 a 9: ')
        if n.isnumeric():
            print(f'Você digitou o numero {n}')
            break
        else:
            print('Numero inválido!')

leiaint()
