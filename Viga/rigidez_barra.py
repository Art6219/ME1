import numpy as np


def rigidez_barra(E, A, L):

    # Calcula a Matriz de Rigidez Local de uma Barra
    Kl = E*A / L * np.array([[1, 0, -1, 0],
                             [0, 0, 0, 0],
                             [-1, 0, 1, 0],
                             [0, 0, 0, 0]])
    
    return Kl

