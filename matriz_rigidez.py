import numpy as np

from rigidez_barra import rigidez_barra
from matriz_transformacao import matriz_transformacao


def matriz_rigidez(nn, ne, conect, VE, VA, Vl, Vr):

    # Cria a Matriz Global
    K = np.zeros((2*nn, 2*nn))

    # Monta a Matriz de Rigidez Global
    for i in range(ne):

        # Recupera valores do elemento
        E = VE[i]
        A = VA[i]
        L = Vl[i]
        theta = Vr[i]

        # Matriz de Rigidez Local
        Kl = rigidez_barra(E, A, L)

        # Matriz de Transformação
        T = matriz_transformacao(theta)

        # Calcula Matriz de Rigidez Global
        Kg = np.linalg.multi_dot([T.transpose(), Kl, T])

        # Calcula Posionamento da Matriz do Elemento na Matriz Global
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Vetor dos Graus de Liberdade Globais do Elemento
        # gls = [2*(node1 - 1) + 1, 2*(node1 - 1) + 2, 2*(node2 - 1) + 1, 2*(node2 - 1) + 2]
        gls = [2*(node1) + 1, 2*(node1) + 2, 2*(node2) + 1, 2*(node2) + 2]

        # Atualiza Matriz de Rigidez
        for i in gls:
            for j in gls:
                K[i - 1, j - 1] += Kg[gls.index(i), gls.index(j)]
    
    return K