def coordenadas(ele_type, conect, coord):

    # Seleciona os nós do elemento
    if ele_type == 1 or ele_type == 2:
        node1 = conect[0]
        node2 = conect[1]
        node3 = conect[2]
        node4 = conect[3]

        nodes = [node1, node2, node3, node4]

        X = [coord[node1][0], coord[node2][0], coord[node3][0], coord[node4][0]]
        Y = [coord[node1][1], coord[node2][1], coord[node3][1], coord[node4][1]]

    elif ele_type == 3:
        node1 = conect[0]
        node2 = conect[1]
        node3 = conect[2]

        nodes = [node1, node2, node3]
        
        X = [coord[node1][0], coord[node2][0], coord[node3][0]]
        Y = [coord[node1][1], coord[node2][1], coord[node3][1]]

        
    return X, Y, nodes