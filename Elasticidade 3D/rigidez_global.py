import numpy as np

from coordenadas import coordenadas
from rigidez_local import rigidez_local
from gls_globais import gls_globais


def rigidez_global(nn, ne, coord, conect, VE, Vv, hip, ele_type):

    # Cria a Matriz de Rigidez Global
    K = np.zeros((3*nn, 3*nn))

    # Monta a Matriz de Rigidez Global
    for i in range(ne):

        # Recupera dados do elemento
        E = VE[i]
        v = Vv[i]

        # Seleciona os nós do elemento
        X, Y, Z, nodes = coordenadas(conect[i], coord)

        # Matriz de Rigidez Local
        Kl = rigidez_local(ele_type[i], X, Y, Z, E, v, hip)

        # Vetor dos Graus de Liberdade Globais do Elemento
        gls = gls_globais(nodes)

        # Atualiza Matriz de Rigidez Global
        for i in gls:
            for j in gls:
                K[i - 1, j - 1] += Kl[gls.index(i), gls.index(j)]
    
    return K