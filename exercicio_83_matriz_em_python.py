lista = list()
dados = list()
valores_pares = list()
soma_3col = list()
maior = 0
for i in range (3):
    n1 = int(input(f'Digite um numero para [{i},{0}]: '))
    dados.append(n1)
    n2 = int(input(f'Digite um numero [{i},{1}]: '))
    dados.append(n2)
    n3 = int(input(f'Digite um numero [{i},{2}]: '))
    dados.append(n3)
    lista.append(dados[:])
    dados.clear()
for i in range (3):
    for j in range (1):
        print(f'[{lista[i][j]}] [{lista[i][j + 1]}] [{lista[i][j + 2]}]')
    i += 1

for i in range (3):
    for j in range (3):
        if lista[i][j] % 2 == 0:
            valores_pares.append(lista[i][j])
        if i == 1 and maior < lista [i][j] :
            maior = lista[i][j]
        if i == 2:
            soma_3col.append(lista[i][j])

print(sum(valores_pares))
print(sum(soma_3col))
print(maior)
