import matplotlib.pyplot as plt

from gradient import gradient
from coordenadas import coordenadas


def plot(coord, conect, ne, nn, U, ele_type, sigmas):

    cores, sigmaxx = gradient(sigmas)

    # Plot
    plt.figure()

    # Calcula os nós com os deslocamentos
    xn = []
    yn = []
    for i in range(nn):

        xn.append(coord[i][0] + U[3*i])
        yn.append(coord[i][1] + U[3*i + 1])

        # Plot pontos da estrutura
        plt.scatter(coord[i][0], coord[i][1], color = 'blue')
        plt.text(coord[i][0], coord[i][1], i + 1, fontweight = 1000)

    # Organiza os pontos dos elementos originais e finais
    Xm = []
    Ym = []
    Zm = []
    Xmd = []
    Ymd = []
    Zmd = []
    for i in range(ne):

        # Coordenadas dos nós originais
        X, Y, Z, nodes = coordenadas(conect, coord)

        xm = sum(X)/len(X)
        ym = sum(Y)/len(Y)
        zm = sum(Z)/len(Z)

        # Coordenadas dos nós deslocados
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
        Zm.append(zm)

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
    

