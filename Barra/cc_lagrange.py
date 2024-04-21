import numpy as np


def cc_lagrange(nn, cc, K, F):   

    # Número de GLs do problema original
    n = 2*nn

    # Número de cc essenciais
    m = len(cc)

    # Define o sistema aumentado de equações
    Ka = np.zeros((n + m, n + m))
    Fa = np.zeros(n + m)

    # Define a matriz auxiliar e o vetor U auxiliar
    S  = np.zeros((m, n))
    Ub = np.zeros(m)

    # Aplica as CC essenciais
    for i in range(m):

        # NÓ e GL local do apoio
        node  = cc[i][0]
        gll = cc[i][1]
        CC = cc[i][2]

        # Gl global
        gl = (2*(node) + gll) - 1

        # Posiciona na linha da matriz S
        S[i, gl] = 1

        # Posiciona o valor em Ub
        Ub[i] = CC

    # Posiciona os blocos na matriz aumentada e no vetor aumentados
    Ka[0: n, 0: n] = K.copy()
    Ka[0: n, n + 0: n + m] = S.transpose().copy()
    Ka[n: n + m, 0: n] = S.copy()

    Fa[0: n] = F.copy()
    Fa[n: n + m] = Ub.copy()

    return Ka, Fa