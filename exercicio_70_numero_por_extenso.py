numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oitava", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    n = int(input('Digite um numero entre 0 e 20: '))

    if n >= 0 and n <= 20:
        print(f'O numero {n} por extenso é {numeros_extenso[n]}')
    else:
        print('Numero fora do intervalo!')
        break
