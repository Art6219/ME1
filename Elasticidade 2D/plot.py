import matplotlib.pyplot as plt

from gradient import gradient


def plot(coord, conect, ne, nn, U, ele_type, sigmas):

    cores, sigmaxx = gradient(sigmas)

    # Plot
    plt.figure()

    # Calcula os nós com os deslocamentos
    xn = []
    yn = []
    for i in range(nn):

        xn.append(coord[i][0] + U[2*i])
        yn.append(coord[i][1] + U[2*i + 1])

        # Plot pontos da estrutura
        plt.scatter(coord[i][0], coord[i][1], color = 'blue')
        plt.text(coord[i][0], coord[i][1], i + 1, fontweight = 1000)

    # Organiza os pontos dos elementos originais e finais
    Xm = []
    Ym = []
    Xmd = []
    Ymd = []
    for i in range(ne):

        # Seleciona os nós do elemento
        if ele_type[i] == 1 or ele_type[i] == 2:
            node1 = conect[i][0]
            node2 = conect[i][1]
            node3 = conect[i][2]
            node4 = conect[i][3]

        elif ele_type[i] == 3:
            node1 = conect[i][0]
            node2 = conect[i][1]
            node3 = conect[i][2]

        # Coordenadas dos elementos originais
        if ele_type[i] == 1 or ele_type[i] == 2:
            x1 = coord[node1][0]
            y1 = coord[node1][1]

            x2 = coord[node2][0]
            y2 = coord[node2][1]

            x3 = coord[node3][0]
            y3 = coord[node3][1]

            x4 = coord[node4][0]
            y4 = coord[node4][1]

            X = [x1, x2, x3, x4, x1]
            Y = [y1, y2, y3, y4, y1]

            xm = (x1 + x2 + x3 + x4)/4
            ym = (y1 + y2 + y3 + y4)/4

        elif ele_type[i] == 3:
            x1 = coord[node1][0]
            y1 = coord[node1][1]

            x2 = coord[node2][0]
            y2 = coord[node2][1]

            x3 = coord[node3][0]
            y3 = coord[node3][1]

            X = [x1, x2, x3, x1]
            Y = [y1, y2, y3, y1]

            xm = (x1 + x2 + x3)/3
            ym = (y1 + y2 + y3)/3

        # Coordenadas dos elementos deslocados
        if ele_type[i] == 1 or ele_type[i] == 2:
            x1d = xn[node1]
            y1d = yn[node1]

            x2d = xn[node2]
            y2d = yn[node2]

            x3d = xn[node3]
            y3d = yn[node3]

            x4d = xn[node4]
            y4d = yn[node4]

            Xd = [x1d, x2d, x3d, x4d, x1d]
            Yd = [y1d, y2d, y3d, y4d, y1d]

            xmd = (x1d + x2d + x3d + x4d)/4
            ymd = (y1d + y2d + y3d + y4d)/4

        elif ele_type[i] == 3:
            x1d = xn[node1]
            y1d = yn[node1]

            x2d = xn[node2]
            y2d = yn[node2]

            x3d = xn[node3]
            y3d = yn[node3]
            
            Xd = [x1d, x2d, x3d, x1d]
            Yd = [y1d, y2d, y3d, y1d]

            xmd = (x1d + x2d + x3d)/3
            ymd = (y1d + y2d + y3d)/3

        Xm.append(xm)
        Ym.append(ym)

        Xmd.append(xmd)
        Ymd.append(ymd)

        # Plot estrutura original
        plt.plot(X, Y, color = 'blue')

        # Plot estrutura deslocada
        plt.plot(Xd, Yd, color = 'red', linestyle = "--")

        # Plot gradiente de tensão
        plt.fill_between(X, Y, color = cores[i])

    # Plot gradiente 
    plt.scatter(Xm, Ym, c = sigmaxx, cmap = "coolwarm")

    cbar = plt.colorbar(format = "%.3f")
    cbar.set_label(label = "σxx")
    

