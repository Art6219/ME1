import numpy as np


def cc_linha(nn, cc, K, F):

    # Seleciona nós com condições de contorno
    dispvect = np.ones((2 * nn, 1), dtype = float)       # Vetor Deslocamento

    for i in range(len(cc)):
        dispvect[cc[i][0] * 2 - 1 + cc[i][1], 0] = cc[i][2]

    rcdlist = []
    for j in range(nn * 2):                              # Verifica em quais posições o deslocamento é nulo
        if dispvect[j, 0] == 0: 
            rcdlist.append(j)

    rrgsm = np.delete(K, rcdlist, 0)                      # Simplificação de Linhas Matriz Global
    crgsm = np.delete(rrgsm, rcdlist, 1)                    # Simplificação de Colunas Matriz Global
    rgsm = crgsm                                            # Matrizde Rigidez Global Reduzida
    rforcevect = np.delete(F, rcdlist, 0)           # Matriz de Froças Global Reduzida

    return rgsm, rforcevect