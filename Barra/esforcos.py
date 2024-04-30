import numpy as np

from matriz_transformacao import matriz_transformacao
from rigidez_barra import rigidez_barra


def esforcos(ne, conect, VE, VA, VL, Vr, U):

    # Cria o vetor dos esforços internos
    N = np.zeros(ne)

    # Loop pelos elementos
    for i in range(ne):

        # Recupera os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Vetor com os GLs globais do elemento
        gls = [2*(node1), 2*(node1) + 1, 2*(node2), 2*(node2) + 1]

        # Vetor de deslocamentos nos nós do elemento 
        Uge = U[gls]

        # Rortação do sistema local em relação ao global
        te = Vr[i]

        # Monta a matriz de transformação T
        T = matriz_transformacao(te)

        # Passa os deslocamentos para o sistema local
        Ule = np.dot(T, Uge)

        # Recupera as informações do elemento
        Ee = VE[i]
        Ae = VA[i]
        Le = VL[i]

        # Monta a matriz de rigidez do elemento no sistema local
        Kle = rigidez_barra(Ee, Ae, Le)

        # Calcula o esforço interno do elemento 
        Fle = np.dot(Kle, Ule)
 
        N[i] = -Fle[0]

    return N