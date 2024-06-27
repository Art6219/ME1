import numpy as np

from constitiva import constitutiva
from B_bolha import B_bolha

def rigidez_elast3d_bolha(X, Y, Z, E, v, hip):
    
    # Cria a matriz de rigidez do elemento
    K = np.zeros((33, 33))

    # Monta a matriz constitutiva
    C = constitutiva(E, v, hip)

    # Método da quadratura 
    pg = [-1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3)]        # Pontos de Gauss
    w = [1, 1, 1]                                           # Peso de quadratura

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
                dJ, B = B_bolha(r, s, t, X, Y, Z)

                # Monta a matriz de rigidez do elemento
                K += np.linalg.multi_dot((B.transpose(), C, B))*dJ

    # Separa a matriz de rigidez
    Kaa = K[0:24, 0:24]
    Kab = K[0:24, 24:33]
    Kba = K[24:33, 0:24]
    Kbb = K[24:33, 24:33]

    # Monta matriz de rigidez equivalente pelo método de redução de Guyan
    Ke = Kaa - np.dot(Kab, np.dot(np.linalg.inv(Kbb), Kba))

    return Ke, Kbb, Kba