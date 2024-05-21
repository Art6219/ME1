import numpy as np

from matriz_transformacao import matriz_transformacao

def forca(conect, nn, loads, Load_dist, VL, Vr):

    # Cria vetor de forças concentradas
    Fc = np.zeros(3*nn)

    # Monta o vetor de força pontual global
    for i in range(len(loads)):
        
        # Seleciona o nó, GL local e valor da força
        node = loads[i][0]
        gll = loads[i][1]
        load = loads[i][2]

        # Atualiza vetor de forças global
        Fc[(3*(node) + gll) - 1] += load

    # Cria o vetor de forças distribuidas
    Fd = np.zeros(3*nn)

    # Monta o vetor de força distribuida global
    for i in range(len(Load_dist)):

        q1 = Load_dist[i][1]
        q2 = Load_dist[i][2]
        ele = Load_dist[i][0]

        L = VL[ele]
        theta = Vr[ele]

        # Monta o vetor local Fqe
        Fdn = [0,  (3*L*q2 + 7*L*q1)/20, (2*L**2*q2 + 3*L**2*q1)/60, 0, (7*L*q2 + 3*L*q1)/20, -((3*L**2*q2 + 2*L**2*q1)/60)]

        # Monta a matriz de transformação T
        T = matriz_transformacao(theta)

        # Rotaciona do sistema local para o global
        # usa T transposto pois estamos passando 
        # do local para o global
        Fqge = np.dot(T.transpose(), Fdn)

        # Recupera os nós do elemento
        node1 = conect[ele][0]
        node2 = conect[ele][1]

        # Vetor com os gls GLOBAIS do elemento
        gls = [3*(node1), 3*(node1) + 1, 3*(node1) + 2, 3*(node2), 3*(node2) + 1, 3*(node2) + 2]

        # Sobrepoe Fqge nas posições globais de Fq
        for j in gls:
            Fd[j] = Fd[j] + Fqge[gls.index(j)]

    F = Fc + Fd

    return F
