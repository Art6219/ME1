import numpy as np


def cc_lagrange(nn, cc, K, F):   

    # Número de gls do problema original
    n = 2*nn

    # Número de cc essenciais
    m = len(cc)

    # Define o sistema aumentado de equações
    Ka = np.zeros((n + m, n + m))
    Fa = np.zeros(n + m)

    # Define a matriz S e o vetor Ub
    S  = np.zeros((m, n))
    Ub = np.zeros(m)

    # Aplica as condições de contorno essenciais
    for i in range(m):

        # No e gl local do apoio
        node  = cc[i][0]
        gll = cc[i][1]
        CC = cc[i][2]

        # Gl global
        gl = (2*(node) + gll) - 1

        # Posiciona na linha da matriz S
        S[i, gl] = 1

        # Posiciona o valor em Ub
        Ub[i] = CC

    # Posiciona os blocos na matriz e no vetor aumentados
    Ka[0: n, 0: n] = K.copy()
    Ka[0: n, n + 0: n + m] = S.transpose().copy()
    Ka[n: n + m, 0: n] = S.copy()

    Fa[0: n] = F.copy()
    Fa[n: n + m] = Ub.copy()

    return Ka, Fa