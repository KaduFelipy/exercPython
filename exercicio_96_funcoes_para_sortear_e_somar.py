from random import randint

numeros = list()

def somar (*n):
    print(f'A soma dos valores pares de {n}, temos {sum([i for i in n if i % 2 == 0])}')

for i in range(5):
    numeros.append(randint(0,9))
    i =+i
print(f'Sorteado {len(numeros)} valores da lista: {numeros}')

print('-='*30)

somar(*numeros)
