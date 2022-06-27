info = dict()
def notas(*notas, sit=False):
    soma = 0
    info['total'] = len(notas)
    info['maior'] = max(notas)
    info['menor'] = min(notas)
    for nota in notas:
        soma += nota
    info['média'] = soma / info['total']
    if sit == True:
        if info['média'] <= 3:
            info['situação'] = 'RUIM'
        elif info['média'] <= 6:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['situação'] = 'BOM'
    print(info)

