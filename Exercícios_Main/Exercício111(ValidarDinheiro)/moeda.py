
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
    porcentonegativo = valor - ((taxa / 100) * valor)
    if format == True:
        return formatar(porcentonegativo)
    else:
        return porcentonegativo


def formatar(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preçodoproduto, taxaa=10, taxar=5):
    l()
    print(f'{"RESUMO DO VALOR".center(30)}')
    l()
    print(f'Preço analisado: \t{formatar(preçodoproduto)}')
    print(f'Dobro do preço: \t{dobro(preçodoproduto, True)}')
    print(f'Metade preço: \t\t{metade(preçodoproduto, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preçodoproduto, taxaa, True)}')
    print(f'{taxar}% de redução: \t{redução(preçodoproduto, taxar, True)}')

def l():
    print('-' * 30)

