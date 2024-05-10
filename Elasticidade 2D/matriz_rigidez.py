import numpy as np

from rigidez_elast2d import rigidez_elast2d


def matriz_rigidez(nn, ne, coord, conect, VE, Vv, esp, hip):

    # Cria a Matriz de Rigidez Global
    K = np.zeros((2*nn, 2*nn))

    # Monta a Matriz de Rigidez Global
    for i in range(ne):

        # Recupera dados do elemento
        E = VE[i]
        v = Vv[i]

        # Seleciona os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]
        node3 = conect[i][2]
        node4 = conect[i][3]

        X = [coord[node1][0], coord[node2][0], coord[node3][0], coord[node4][0]]
        Y = [coord[node1][1], coord[node2][1], coord[node3][1], coord[node4][1]]

        # Matriz de Rigidez Local
        Kl = rigidez_elast2d(X, Y, esp, E, v, hip)

        # Vetor dos Graus de Liberdade Globais do Elemento
        gls = [2*(node1) + 1, 2*(node1) + 2, 2*(node2) + 1, 2*(node2) + 2, 2*(node3) + 1, 2*(node3) + 2, 2*(node4) + 1, 2*(node4) + 2]

        # Atualiza Matriz de Rigidez Global
        for i in gls:
            for j in gls:
                K[i - 1, j - 1] += Kl[gls.index(i), gls.index(j)]
    
    return K