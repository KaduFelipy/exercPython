numeros = []
for i in range (5):
    n = int(input('Digite um numero: '))
    numeros.append(n)
print(f'O maior numero é {max(numeros)} e está na posição {numeros.index(max(numeros))}')
print(f'O menor numero é {min(numeros)} e está na posição {numeros.index(min(numeros))}')
