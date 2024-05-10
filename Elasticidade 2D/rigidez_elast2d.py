import numpy as np

from constitiva import constitutiva
from B_bi4n import B_bi4n

def rigidez_elast2d(X, Y, esp, E, v, hip):
    
    # Cria a matriz de rigidez do elemento
    K = np.zeros((8, 8))

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
           dJ, B = B_bi4n(r, s, X, Y)

           # Monta a matriz de rigidez do elemento
           K += np.linalg.multi_dot((B.transpose(), C, B))*dJ*esp

    return K