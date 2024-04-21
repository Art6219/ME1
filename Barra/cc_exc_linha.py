import numpy as np


def cc_exc_linha(nn, cc, K, F):

    # Cria um vetor auxiliar de deslocamento
    desloc = np.ones((2*nn, 1), dtype = float)

    for i in range(len(cc)):
        desloc[cc[i][0] * 2 - 1 + cc[i][1], 0] = cc[i][2]

    # Seleciona GL com CC
    GL_rest = []
    for j in range(2*nn):                           
        if desloc[j, 0] == 0: 
            GL_rest.append(j)

    K_row = np.delete(K, GL_rest, 0)                # Simplificação de Linhas Matriz Global
    K_collumn = np.delete(K_row, GL_rest, 1)        # Simplificação de Colunas Matriz Global
    Kn = K_collumn                                  # Matrizde Rigidez Global Reduzida
    Fn = np.delete(F, GL_rest, 0)                   # Matriz de Froças Global Reduzida

    return Kn, Fn