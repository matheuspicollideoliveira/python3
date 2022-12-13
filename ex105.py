def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos aceitas
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict()
    turma['total'] = len(num)
    turma['maior'] = max(num)
    turma['menor'] = min(num)
    turma['media'] = sum(num)/len(num)
    if sit:
        if turma['media'] < 5:
            turma['situação'] = 'RUIM'
        elif turma['media'] >= 7:
            turma['situação'] = 'BOA'
        else:
            turma['situação'] = 'RAZOÁVEL'
    return turma


resp = notas(5, 10, 2, 8, 10, 8, sit=True)
print(resp)
