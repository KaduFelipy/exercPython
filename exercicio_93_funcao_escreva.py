p = str(input('Digite algo: '))

def escreva(p):
    comprimento = len(p) + 4
    print('-'*comprimento)
    print(p.center(comprimento))
    print('-'*comprimento)

escreva(p)
