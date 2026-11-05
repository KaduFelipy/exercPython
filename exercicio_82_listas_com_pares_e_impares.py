par = list()
impar = list()

for i in range (7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
impar.sort()
par.sort()
print(f'numeros impares {impar}')
print(f'numeros pares {par}')
