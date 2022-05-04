def verifica_ordenacao_topologica(grafo, ordem_topologica):
    """
    Verifica se uma ordenação topológica é válida.
    """
    vnum = {}
    for i in range(len(ordem_topologica)):
        if ordem_topologica[i] not in grafo:
            return False
        vnum[ordem_topologica[i]] = i

    for v in grafo:
        if v not in vnum:
            return False
        for w in grafo[v]:
            if w not in vnum or vnum[w] <= vnum[v]:
                return False
    return True