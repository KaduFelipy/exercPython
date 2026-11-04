lista = []
while True:
    n = int(input('Digite um numero'))
    if n in lista:
        print('Valor duplicado!')
        continue
    else:
        lista.append(n)
    p = input('Quer continuar? [S/N]')
    p.lower()
    if p == 'n':
        break
    elif p == 's':
        continue

lista_ordenada = sorted(lista)
print(lista_ordenada)
