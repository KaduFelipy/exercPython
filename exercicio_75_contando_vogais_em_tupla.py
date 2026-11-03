tupla = ('ovo', 'cafe', 'tomate', 'leite', 'pao')
vogais = 'aeiou'

for palavra in tupla:
    vogais_da_palavra = ' '.join([l for l in palavra if l in vogais])
    print(f'{palavra} tem as seguintes vogais: {vogais_da_palavra}')
