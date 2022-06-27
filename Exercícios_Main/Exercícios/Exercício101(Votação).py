from datetime import date


def votar(ano):
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade}, o voto é OPCIONAL'
    elif idade >= 18:
        return f'Com {idade}, o voto é OBRIGATÓRIO'
    else:
        return f'Com {idade}, o voto é NEGADO'

ano = int(input('Digite seu ano de nascimento: '))
print(votar(ano))


