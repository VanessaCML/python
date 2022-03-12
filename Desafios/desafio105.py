def notas(*n, sit=False):
    """
    -> Análise de notas de alunos
    :param n: Notas dos alunos (aceita várias entradas)
    :param sit: Exibe ou não a situação da média da turma (opcional)
    :return: Retorna dicionário com as informações completas da turma
    """
    lista = {}
    lista['qtde'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['média'] = sum(n) / len(n)
    if sit:
        if lista['média'] < 6:
            lista['situação'] = 'RUIM'
        else:
            lista['situação'] = 'BOA'
    return lista


resp = notas(4, 6, 8, 7, 2.4, 6.3, 9.5)
print(resp)
help(notas)
