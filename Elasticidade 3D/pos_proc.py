import numpy as np

from coordenadas import coordenadas
from gls_globais import gls_globais
from B_bolha import B_bolha
from B_ti8n import B_ti8n
from constitiva import constitutiva
from rigidez_elast3d_bolha import rigidez_elast3d_bolha


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
        X, Y, Z, nodes = coordenadas(conect[i], coord)

        # Vetor dos Graus de Liberdade Globais do Elemento
        gls = gls_globais(nodes)

        # Vetor de deslocamentos globais nos nós do elemento
        for j in range(len(gls)):
            gls[j] = gls[j] - 1

        Uge = U[gls]

        # Calculo matriz B
        if ele_type[i] == 1:

            _, B = B_ti8n(0, 0, 0, X, Y, Z)
        
        elif ele_type[i] == 2:

            _, B = B_bolha(0, 0, 0, X, Y, Z)

            if i == 0:
                _, Kbb, Kba = rigidez_elast3d_bolha(X, Y, Z, E, v, hip)

            alpha = np.linalg.multi_dot([-np.linalg.inv(Kbb), Kba, Uge])

            Uge = np.concatenate((Uge, alpha))

        # Calcula deformação em cada elemento
        e = np.dot(B, Uge)

        # Monta a matriz constitutiva do elemento
        C = constitutiva(E, v, hip)

        # Calcula a tensão em cada elemento
        sigma = np.dot(C, e)

        eps.append(e)
        sigmas.append(sigma)


    return eps, sigmas