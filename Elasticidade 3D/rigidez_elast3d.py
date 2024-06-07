import numpy as np

from constitiva import constitutiva
from B_ti8n import B_ti8n


def rigidez_elast3d(X, Y, Z, E, v, hip):
    
    # Cria a matriz de rigidez do elemento
    K = np.zeros((24, 24))

    # Monta a matriz constitutiva
    C = constitutiva(E, v, hip)

    # Método da quadratura 
    pg = [-1/np.sqrt(3), 1/np.sqrt(3)]      # Pontos de Gauss
    w = [1, 1]                              # Peso de quadratura

    for i in range(2):

        r = pg[i]
        wr = w[i]

        for j in range(2):

            s = pg[j]  
            ws = w[j]

            for k in range(2):

                t = pg[k]
                wk = w[k]

                # Calcula o determinante da matriz Jacobiana e a matriz B
                dJ, B = B_ti8n(r, s, t, X, Y, Z)

                # Monta a matriz de rigidez do elemento
                K += np.linalg.multi_dot((B.transpose(), C, B))*dJ

    return K