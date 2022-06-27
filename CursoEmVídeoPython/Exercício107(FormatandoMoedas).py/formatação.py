def metade(valor):
    metade = valor / 2
    return formatar(metade)


def dobro(valor):
    dobro = valor * 2
    return formatar(dobro)

def pct(valor, taxa):
    dezporcento = ((taxa / 100) * valor) + valor
    return formatar(dezporcento)

def formatar(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


