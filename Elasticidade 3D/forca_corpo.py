import numpy as np

from coordenadas import coordenadas
from gls_globais import gls_globais
from N_ti8n import N_ti8n
from B_ti8n import B_ti8n

def forca_corpo(rho, g, conect, coord, F):

    b = np.array([0, 0, -rho*g])

    for i in range(len(conect)):

        X, Y, Z, nodes = coordenadas(conect[i], coord)

        gls = gls_globais(nodes)

        Fbe = np.zeros(24)

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

                    dJ, _ = B_ti8n(r, s, t, X, Y, Z)

                    Ni = N_ti8n(r, s, t)

                    Fbe += np.dot(Ni.transpose(), b)*dJ
    
        for j in gls:
            F[j - 1] += Fbe[gls.index(j)]

    return F
