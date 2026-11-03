valor1 = int(input('Digite um numero: '))
valor2 = int(input('Digite outro numero: '))
valor3 = int(input('Digite outro numero: '))
valor4 = int(input('Digite outro numero: '))
tupla = (valor1,valor2,valor3,valor4)

print(tupla.count(9))
print(tupla.index(3))
for i in tupla:
    if i % 2 == 0:
        lista=[]
        lista.append(i)
print(lista)
