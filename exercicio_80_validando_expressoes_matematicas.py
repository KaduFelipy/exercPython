expr = input('Digite a expressão: ')
conchete = 0
for i in expr:
    if i == '(':
        conchete = conchete + 1
    elif i == ')':
        conchete = conchete - 1
if conchete == 0:
    print(f'A expressão {expr} é válida!')
else:
    print(f'A expressão {expr} é inválida!')
