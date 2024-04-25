import numpy as np


def matriz_transformacao(theta):

    # Calcula sen e cos
    s = np.sin(theta)
    c = np.cos(theta)

    # Monta a Matriz de Rotação
    T = np.array([[c, s, 0, 0, 0, 0],
                  [-s, c, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, c, s, 0],
                  [0, 0, 0, -s, c, 0],
                  [0, 0, 0, 0, 0, 1]])
    
    return T
