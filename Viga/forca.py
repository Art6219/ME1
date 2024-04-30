import numpy as np


def forca(nn, loads, Load_dist, VL, Vr):

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

        ele = Load_dist[i][0]

        q1 = Load_dist[i][1]
        q2 = Load_dist[i][2]
        L = VL[ele]
        theta = Vr[ele]

        # Flata montar o vetor com os calculos prontos, transformar de local para global e somar com força_concentrada

    F = Fc + Fd
    return F