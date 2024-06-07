import numpy as np


def gls_globais(nodes):

    # Cria o vetor de graus de liberdade
    gls = []

    # Monta vetor de graus de liberdade
    for i in range(len(nodes)):
        for j in range(2):

            gls.append(int(2*nodes[i] + (j + 1)))

    return gls





