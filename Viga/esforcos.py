import numpy as np

from matriz_transformacao import matriz_transformacao
from matriz_rigidez import matriz_rigidez


def esforcos(nn, ne, conect, VE, VA, VL, VI, Vr, U, loads_dist):

    # Aloca o vetor de esforços normais
    N = np.zeros(ne)

    # Aloca um vetor de vetores
    V = []
    M = []

    # Loop pelos elementos
    for ele in range(ne):

        # Recupera os nós do elemento
        node1 = conect[ele][1]
        node2 = conect[ele][2]

        # Vetor com os gls GLOBAIS do elemento
        gls = [3*(node1), 3*(node1) + 1, 3*(node1) + 2, 3*(node2), 3*(node2) + 1, 3*(node2) + 2]

        # Vetor de deslocamentos nos nós do elemento e 
        # ainda no sistema global de referência 
        Uge = U[gls]

        # ângulo do sistema local em relação ao global
        te = Vr[ele]

        # Monta a matriz de transformação T
        T = matriz_transformacao(te)

        # Passa Uge para o sistema local de referência
        Ule = np.dot(T, Uge)

        # Recupera as informações do elemento
        Ee = VE[ele]
        Ie = VI[ele]
        Ae = VA[ele]
        Le = VL[ele]

        # Monta a matriz de rigidez do elemento no sistema local
        Kle = matriz_rigidez(nn, ne, conect, VE, VA, VI, VL, Vr)

        # Calcula o vetor de forças nodais do elemento 
        # no sistema local
        Fle = np.dot(Kle, Ule)

        # Esforço normal interno do elemento é 
        N[ele] = -Fle[0]

        # Dados para gerar os gráficos dos elementos
        xe = range(0, Le, 100)

        # Procura se existe alguma informação sobre o elemento
        # em loads_dist
        for i in range(len(loads_dist)):
            if (loads_dist[i][0]) == ele:
                q1 = loads_dist[i][1]
                q2 = loads_dist[i][2]
                break

        # Esforço cortante do elemento
        fc(x) = -(((q2-q1)*x^2+2*Le*q1*x+2*Fle[2]*Le)/(2*Le))
        ve = fc.(xe)
        append!(V, [ve])

        # Momento do elemento
        fm(x) = ((q2-q1)*x^3+3*Le*q1*x^2+6*Fle[2]*Le*x-6*Fle[3]*Le)/(6*Le)
        me =  fm.(xe)
        append!(M,[me])

    end

    # Retorna os esforços em cada elemento
    return N, V, M