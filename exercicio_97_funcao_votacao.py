def votacao(n):
    if 2026 - n >= 18:
        return 'O voto é obrigatório'

    elif 2026 - n >= 16 and 2026 - n <= 17:
        return 'O voto é opcional'
    else:
        return 'Voto negado'

nasc = int(input('Em que ano você nasceu? '))

votacao(nasc)
