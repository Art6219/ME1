import numpy as np

from matriz_transformacao import matriz_transformacao
from matriz_rigidez import matriz_rigidez
from rigidez_portico_plano import rigidez_portico_plano


def esforcos(nn, ne, conect, VE, VA, VL, VI, Vr, U, loads_dist):

    # Cria o vetor dos esforços internos
    N = np.zeros(ne)
    V = []
    M = []

    # Loop pelos elementos
    for i in range(ne):

        # Recupera os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Vetor com os gls globais do elemento
        gls = [3*(node1), 3*(node1) + 1, 3*(node1) + 2, 3*(node2), 3*(node2) + 1, 3*(node2) + 2]

        # Vetor de deslocamentos globais nos nós do elemento
        Uge = U[gls]

        # Rotação do sistema local em relação ao global
        te = Vr[i]

        # Monta a matriz de transformação T
        T = matriz_transformacao(te)

        # Deslocamentos no sistema local 
        Ule = np.dot(T, Uge)

        # Recupera as informações do elemento
        E = VE[i]
        I = VI[i]
        A = VA[i]
        L = VL[i]

        # Monta a matriz de rigidez do elemento no sistema local
        Kle = rigidez_portico_plano(E, A, I, L)

        # Calcula os esforços internos do elemento
        Fle = np.dot(Kle, Ule)

        # Esforço normal interno do elemento
        N[i] = -Fle[0]

        # Dados para gerar os gráficos dos elementos
        xe = np.linspace(0, L, 100)

        # Define q2 e q1
        q1 = 0
        q2 = 0
        for i in range(len(loads_dist)):
            if (loads_dist[i][0]) == i:
                q1 = loads_dist[i][1]
                q2 = loads_dist[i][2]
                break
        
        # Calcula o esforço cortante e momento fletor em diversos pontos do elemento
        fc = lambda x, q2, q1, Fle, L: -(((q2 - q1)*x**2 + 2*L*q1*x + 2*Fle[2]*L)/(2*L))
        fm = lambda x, q2, q1, Fle, L: ((q2 - q1)*x**3 + 3*L*q1*x**2 + 6*Fle[2]*L*x - 6*Fle[3]*L)/(6*L)

        # Monta os vetores do esforço cortante e momento fletor
        V.append(fc(xe, q2, q1, Fle, L))
        M.append(fm(xe, q2, q1, Fle, L))


    return N, V, M

