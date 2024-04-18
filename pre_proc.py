import numpy as np


def pre_proc(coord, conect, ne):

    # Cria os vetores de comprimento e rotação
    Vl = np.zeros(ne)
    Vr = np.zeros(ne)

    # Calcula o comprimento e rotação de cada elemento
    for i in range(ne):

        # Seleciona os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Coordenadas do elemento
        x1 = coord[node1][0]
        y1 = coord[node1][1]

        x2 = coord[node2][0]
        y2 = coord[node2][1]

        # Calcula comprimento do elemento
        dx = x2 - x1
        dy = y2 - y1

        Vl[i] = np.sqrt(dx ** 2 + dy ** 2)

        # Calcula a rotação do elemento
        if dx == 0:
            if dy > 0:
                Vr[i] = np.pi / 2

            else:
                Vr[i] = -np.pi / 2

        else:
            Vr[i] = np.arctan(dy / dx)


    return Vl, Vr
