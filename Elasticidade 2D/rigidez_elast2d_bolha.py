import numpy as np

from constitiva import constitutiva
from bolha import bolha

def rigidez_elast2d_bolha(X, Y, esp, E, v, hip):
    
    # Cria a matriz de rigidez do elemento
    K = np.zeros((12, 12))

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

           # Calcula o determinante da matriz Jacobiana e a matriz B
           dJ, B = bolha(r, s, X, Y)

           # Monta a matriz de rigidez do elemento
           K += np.linalg.multi_dot((B.transpose(), C, B))*dJ*esp

    # Separa a matriz de rigidez
    Kaa = K[0:7, 0:7]
    Kab = K[0:7, 8:-1]
    Kba = K[8:-1, 0:7]
    Kbb = K[8:-1, 8:-1]

    # Monta matriz de rigidez equivalente pelo método de redução de Guyan
    Ke = Kaa - np.linalg.multi_dot([Kab, np.linalg.inv(Kbb), Kba])

    return Ke