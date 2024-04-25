import numpy as np


def rigidez_portico_plano(E, A, I, L):

    # Cria matriz de rigidez
    Kl = np.zeros((6, 6))

    # Calcula a Matriz de Rigidez Local (parte barra)
    Cte = E*A / L

    Kl[0, 0] = Cte
    Kl[0, 3] = -Cte
    Kl[3, 0] = -Cte
    Kl[3, 3] = Cte

    # Calcula a Matriz de Rigidez Local (parte viga)
    Cte = E*I / L

    Kl[1, 1] = 12*Cte / L**2
    Kl[1, 2] = 6*Cte / L
    Kl[1, 4] = -Kl[1, 1]
    Kl[1, 5] = Kl[1, 2]

    Kl[2, 1] = Kl[1, 2]
    Kl[2, 2] = 4*Cte
    Kl[2, 4] = -Kl[1, 2]
    Kl[2, 5] = 2*Cte

    Kl[4, 1] = Kl[1, 4]
    Kl[4, 2] = Kl[2, 4]
    Kl[4, 4] = Kl[1, 1]
    Kl[4, 5] = -Kl[1, 2]
    
    Kl[5, 1] = Kl[1, 5]
    Kl[5, 2] = Kl[2, 5]
    Kl[5, 4] = Kl[4, 5]
    Kl[5, 5] = Kl[2, 2]

    return Kl

