import numpy as np


def forca(nn, loads):

    # Cria vetor de forças
    F = np.zeros(2*nn)

    # Monta o vetor de força global
    for i in range(len(loads)):
        
        # Seleciona o nó, GL local e valor da força
        node = loads[i][0]
        gll = loads[i][1]
        load = loads[i][2]

        # Atualiza vetor de forças global
        F[(2*(node) + gll) - 1] += load

    return F