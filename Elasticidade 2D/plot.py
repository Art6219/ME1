import matplotlib.pyplot as plt


def plot(coord, conect, ne, nn, U):

    # Plot
    plt.figure()

    # Calcula os nós com os deslocamentos
    xn = []
    yn = []
    for i in range(nn):

        xn.append(coord[i][0] + U[2*i])
        yn.append(coord[i][1] + U[2*i + 1])

        plt.scatter(coord[i][0], coord[i][1], color = 'blue')
        plt.text(coord[i][0], coord[i][1], i + 1, fontweight = 1000)

    # Organiza os pontos dos elementos originais e finais
    for i in range(ne):

        # Seleciona os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]
        node3 = conect[i][2]
        node4 = conect[i][3]

        # Coordenadas dos elementos originais
        x1 = coord[node1][0]
        y1 = coord[node1][1]

        x2 = coord[node2][0]
        y2 = coord[node2][1]

        x3 = coord[node3][0]
        y3 = coord[node3][1]

        x4 = coord[node4][0]
        y4 = coord[node4][1]

        # Coordenadas dos elementos deslocados
        x1d = xn[node1]
        y1d = yn[node1]

        x2d = xn[node2]
        y2d = yn[node2]

        x3d = xn[node3]
        y3d = yn[node3]

        x4d = xn[node4]
        y4d = yn[node4]

        plt.plot([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color = 'blue')
        plt.plot([x1d, x2d, x3d, x4d, x1d], [y1d, y2d, y3d, y4d, y1d], color = 'red', linestyle = "--")

