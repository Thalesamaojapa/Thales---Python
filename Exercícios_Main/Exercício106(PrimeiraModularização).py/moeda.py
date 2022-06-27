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

def aumento(valor, taxa, format=False):
    porcentopositivo = ((taxa / 100) * valor) + valor
    if format == True:
        return formatar(porcentopositivo)
    else:
        return porcentopositivo

def redução(valor, taxa, format=False):
    porcentonegativo = ((taxa / 100) * valor) - valor
    if format == True:
        return formatar(porcentonegativo)
    else:
        return porcentonegativo


def formatar(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(valor, aumento, redução):
    l()
    print(f'{"RESUMO DO VALOR"^10}')
    l()
    print(f'Preço analisado: {valor:>10}')
    print(f'Dobro do preço: {dobro(valor, True):>10}')
    print(f'Metade preço: {metade(valor, True):>10}')
    print(f'{aumento}% de aumento: {aumento(valor, aumento, True):>10}')
    print(f'{redução}% de redução: {redução(valor, redução, True):>10}')

def l():
    print('-' * 30)
