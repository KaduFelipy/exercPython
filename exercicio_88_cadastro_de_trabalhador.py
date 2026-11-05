dados = dict()

print('='*30)
dados['nome'] = str(input('Digite seu nome: '))
dados['nasc'] = int(input('Digite seu ano de nascimento: '))
dados['ctps'] = int(input('Digite o número da sua CTPS (0 - Não possui CTPS): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano da primeira contratação: '))
    dados['aposentadoria'] = dados['nasc'] + 35
    dados['salario'] = float(input('Digite o salário do primeiro: '))
print('='*30)
for k, v in dados.items():
    print('-'*30)
    print(f'{k} tem o valor {v}')
