def coordenadas(conect, coord):

    nodes = []
    X = []
    Y = []
    Z = []

    for i in range(len(conect)):

        nodes.append(conect[i])

        X.append(coord[nodes[i]][0])
        Y.append(coord[nodes[i]][1])
        Z.append(coord[nodes[i]][2])

    
    return X, Y, Z, nodes





