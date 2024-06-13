import numpy as np


def bolha(r, s, X, Y):

    # Vetores das derivadas das equações de interpolação N's
    dNr = [-0.25*(1 - s), 0.25*(1 - s), 0.25*(1 + s), -0.25*(1 + s)]
    dNs = [-0.25*(1 - r), -0.25*(1 + r), 0.25*(1 + r), 0.25*(1 - r)]

    # Monta a matriz Jacobiana
    J = np.zeros((2, 2))

    for i in range(4):

        J[0, 0] += dNr[i]*X[i]
        J[0, 1] += dNr[i]*Y[i]
        J[1, 0] += dNs[i]*X[i]
        J[1, 1] += dNs[i]*Y[i]

    # Calcula o determinante e inversa da matriz Jacobiana
    dJ = np.linalg.det(J)
    invJ = np.linalg.inv(J)

    # Cria a matriz B
    B = np.zeros((3, 12))

    # Adiciona as funções adicionais
    dNr.append(-2*r)
    dNr.append(0)
    
    dNs.append(0)
    dNs.append(-2*s)

    c = 0                    # Coluna da matriz B

    for i in range(6):
        
        # Correção das derivadas para este bloco
        dN = [[dNr[i]],
              [dNs[i]]]

        dNxy = np.dot(invJ, dN)

        # Monta a matriz B
        B[0, c] = dNxy[0]
        B[1, c + 1] = dNxy[1]
        B[2, c] = dNxy[1]
        B[2, c + 1] = dNxy[0]

        # Atualiza a coluna da matriz
        c += 2

    return dJ, B