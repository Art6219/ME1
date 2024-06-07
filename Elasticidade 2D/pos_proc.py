import numpy as np

from coordenadas import coordenadas
from gls_globais import gls_globais
from bolha import bolha
from B_bi4n import B_bi4n
from constitiva import constitutiva


def pos_proc(coord, conect, ele_type, ne, U, VE, Vv, hip):

    # Cria vetores de deformação e tensão
    eps = []
    sigmas = []

    # Calcual tensão e deformação em cada elemento
    for i in range(ne):

        # Recupera dados do elemento
        E = VE[i]
        v = Vv[i]

        # Seleciona os nós do elemento
        X, Y, nodes = coordenadas(ele_type[i], conect[i], coord)

        # Vetor dos Graus de Liberdade Globais do Elemento
        gls = gls_globais(nodes)

        # Calculo matriz B
        if ele_type[i] == 3:
            x1 = X[0]
            x2 = X[1]
            x3 = X[2]

            y1 = Y[0]
            y2 = Y[1]
            y3 = Y[2]
    
            B = np.array([[-(y3-y2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, (y3-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, -(y2-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0],
                          [0, (x3-x2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, -(x3-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, (x2-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1)],
                          [(x3-x2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(y3-y2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(x3-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), (y3-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), (x2-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(y2-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1)]])
        
        else:
            _, B = B_bi4n(0, 0, X, Y)

        # Vetor de deslocamentos globais nos nós do elemento
        for i in range(len(gls)):
            gls[i] = gls[i] - 1

        Uge = U[gls]

        # Calcula deformação em cada elemento
        e = np.dot(B, Uge)

        # Monta a matriz constitutiva do elemento
        C = constitutiva(E, v, hip)

        # Calcula a tensão em cada elemento
        sigma = np.dot(C, e)

        eps.append(e)
        sigmas.append(sigma)


    return eps, sigmas