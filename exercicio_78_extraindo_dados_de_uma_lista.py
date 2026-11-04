lista = []
for i in range (5):
    n = int(input('Digite um numero: '))
    lista.append(n)
print(len(lista))
lista_ordenada = sorted(lista)
print(lista_ordenada)
if 5 in lista:
    print('O numero 5 está na lista')
