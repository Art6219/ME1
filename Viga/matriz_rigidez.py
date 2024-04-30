import numpy as np

from rigidez_portico_plano import rigidez_portico_plano
from matriz_transformacao import matriz_transformacao


def matriz_rigidez(nn, ne, conect, VE, VA, VI, VL, Vr):

    # Cria a Matriz de Rigidez Global
    K = np.zeros((3*nn, 3*nn))

    # Monta a Matriz de Rigidez Global
    for i in range(ne):

        # Recupera dados do elemento
        E = VE[i]
        A = VA[i]
        I = VI[i]
        L = VL[i]
        theta = Vr[i]

        # Matriz de Rigidez Local
        Kl = rigidez_portico_plano(E, A, I, L)

        # Matriz de Transformação
        T = matriz_transformacao(theta)

        # Calcula Matriz de Rigidez Global
        Kg = np.linalg.multi_dot([T.transpose(), Kl, T])

        # Seleciona os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Vetor dos Graus de Liberdade Globais do Elemento
        gls = [3*(node1), 3*(node1) + 1, 3*(node1) + 2, 3*(node2), 3*(node2) + 1, 3*(node2) + 2]

        # Atualiza Matriz de Rigidez Global
        for i in gls:
            for j in gls:
                K[i, j] += Kg[gls.index(i), gls.index(j)]
    
    return K