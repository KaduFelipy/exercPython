lista = []
listapar = []
listaimpar = []
for i in range (10):
    n = int(input('Digite um numero: '))
    lista.append(n)
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
print(lista)
print(listapar)
print(listaimpar)
