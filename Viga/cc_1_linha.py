import numpy as np


def cc_1_linha(nn, cc, K, F):

    # Cria um vetor auxiliar de deslocamento
    desloc = np.ones((3*nn, 1), dtype = float)

    for i in range(len(cc)):
        desloc[cc[i][0] * 3 - 1 + cc[i][1], 0] = cc[i][2]

    # Seleciona GL com CC
    GL_cc = []
    for j in range(3*nn):                           
        if desloc[j, 0] == 0: 
            GL_cc.append(j)

    # Zera as linhas/colunas dos GLs com CC
    for i in GL_cc:
        K[i] = np.zeros(len(K[0]))

        for j in range(len(K)):
            K[j][i] = 0

    for i in GL_cc:
        K[i][i] = 1

    return K, F