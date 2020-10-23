def notas(*n, sit=False):
    """
    -> função para analisar notas e situação dos alunos
    :param n: digite as notas
    :param sit: digite de se deseja ou não ver a situação [true/false]
    :return: retorna valor
    """
    r = dict()
    r['Total'] = len(n)
    r['Max'] = max(n)
    r['Min'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#programa
resp = notas(5, 6, 7, 8, sit=True)
print(resp)