import numpy as np


def N_ti8n(r, s, t):

    # Pontos utilizados para o elemento mapeado
    """
    1) 1 -1 -1
    2) 1 1 -1
    3) -1 1 -1
    4) -1 -1 -1
    5) 1 -1 1
    6) 1, 1, 1
    7) -1 1 1
    8) -1 -1 1
    """

    Ni = [1/8*(1+r)*(1-s)*(1-t), 1/8*(1+r)*(1+s)*(1-t), 1/8*(1-r)*(1+s)*(1-t), 1/8*(1-r)*(1-s)*(1-t), 1/8*(1+r)*(1-s)*(1+t), 1/8*(1+r)*(1+s)*(1+t), 1/8*(1-r)*(1+s)*(1+t), 1/8*(1-r)*(1-s)*(1+t)]

    N = np.zeros((3, 24))

    c = 0
    
    for i in range(8):

        N[0, c] = Ni[i]
        N[1, c + 1] = Ni[i]
        N[2, c + 2] = Ni[i]

        c += 3

    return N