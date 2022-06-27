def metade(valor, format=False):
    metade = valor / 2
    if format == True:
        return formatar(metade)
    else:
        return metade

def dobro(valor, format=False):
    dobro = valor * 2
    if format == True:
        return formatar(dobro)
    else:
        return dobro

def pct(valor, taxa, format=False):
    dezporcento = ((taxa / 100) * valor) + valor
    if format == True:
        return formatar(dezporcento)
    else:
        return dezporcento

def formatar(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
