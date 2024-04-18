import numpy as np

from matriz_transformacao import matriz_transformacao
from rigidez_barra import rigidez_barra


def esforcos(ne, conect, VE, VA, Vl, Vr, U):

    # Aloca o vetor de esforços normais
    N = np.zeros(ne)

    # Loop pelos elementos
    for i in range(ne):

        # Recupera os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Vetor com os gls GLOBAIS do elemento
        gls = [2*(node1) + 1, 2*(node1) + 2, 2*(node2) + 1, 2*(node2) + 2]

        # Vetor de deslocamentos nos nós do elemento e 
        # ainda no sistema global de referência 
        Uge = U[gls]

        # ângulo do sistema local em relação ao global
        te = Vr[i]

        # Monta a matriz de transformação T
        T = matriz_transformacao(te)

        # Passa Uge para o sistema local de referência
        Ule = T*Uge

        # Recupera as informações do elemento
        Ee = VE[i]
        Ae = VA[i]
        Le = Vl[i]

        # Monta a matriz de rigidez do elemento no sistema local
        Kle = rigidez_barra(Ee, Ae, Le)

        # Calcula o vetor de forças nodais do elemento 
        # no sistema local
        Fle = Kle*Ule

        # Esforço normal interno do elemento é 
        N[i] = -Fle[1].copy()

    return N