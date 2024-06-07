import numpy as np


def B_ti8n(r, s, t, X, Y, Z):
    
    # Pontos utilizados para o elemento mapeado
    """
    1) 1 -1 -1
    2) 1 1 -1
    3) -1 1 -1
    4) -1 -1 -1
    5) 1 -1 1
    6) 1, 1, 1
    7) -1 1 1
    8) -1 -1 1
    """
    
    # Vetores das derivadas das equações de interpolação N's
    dNr = [1/8*(1-s)*(1-t), 1/8*(1+s)*(1-t), -1/8*(1+s)*(1-t), -1/8*(1-s)*(1-t), 1/8*(1-s)*(1+t), 1/8*(1+s)*(1+t), -1/8*(1+s)*(1+t), -1/8*(1-s)*(1+t)]
    dNs = [-1/8*(1+r)*(1-t), 1/8*(1+r)*(1-t), 1/8*(1-r)*(1-t), -1/8*(1-r)*(1-t), -1/8*(1+r)*(1+t), 1/8*(1+r)*(1+t), 1/8*(1-r)*(1+t), -1/8*(1-r)*(1+t)]
    dNt = [-1/8*(1+r)*(1-s), -1/8*(1+r)*(1+s), -1/8*(1-r)*(1+s), -1/8*(1-r)*(1-s), 1/8*(1+r)*(1-s), 1/8*(1+r)*(1+s), 1/8*(1-r)*(1+s), 1/8*(1-r)*(1-s)]

    # Monta a matriz Jacobiana
    J = np.zeros((3, 3))

    for i in range(8):
        
            J[0, 0] += dNr[i]*X[i]
            J[0, 1] += dNr[i]*Y[i]
            J[0, 2] += dNr[i]*Z[i]

            J[1, 0] += dNs[i]*X[i]
            J[1, 1] += dNs[i]*Y[i]
            J[1, 2] += dNs[i]*Z[i]

            J[2, 0] += dNt[i]*X[i]
            J[2, 1] += dNt[i]*Y[i]
            J[2, 2] += dNt[i]*Z[i]

    # Calcula o determinante e inversa da matriz Jacobiana
    dJ = np.linalg.det(J)
    invJ = np.linalg.inv(J)

    # Cria a matriz B
    B = np.zeros((6, 24))

    c = 0                    # Coluna da matriz B

    for i in range(8):
        
        # Correção das derivadas para este bloco
        dN = [[dNr[i]],
                [dNs[i]],
                [dNt[i]]]
        
        dNxy = np.dot(invJ, dN)

        # Monta a matriz B
        B[0, c] = dNxy[0]
        B[1, c + 1] = dNxy[1]
        B[2, c + 2] = dNxy[2]

        B[3, c + 1] = dNxy[2]
        B[3, c + 2] = dNxy[1]

        B[4, c] = dNxy[2]
        B[4, c + 2] = dNxy[0]

        B[5, c] = dNxy[1]
        B[5, c + 1] = dNxy[0]

        # Atualiza a coluna da matriz
        c += 3

    return dJ, B