import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from gradient import gradient
from coordenadas import coordenadas


def plot(coord, conect, ne, nn, U, sigmas):

    plot_original = False
    plot_desloc = True
    plot_nodes_original = False
    plot_nodes_desloc = False

    cores, sigmaxx = gradient(sigmas)

    # Criação da figura deslocada
    if plot_original is True:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    
    if plot_desloc is True:
        figd = plt.figure()
        axd = figd.add_subplot(111, projection='3d')
    
    # Calcula os nós com os deslocamentos
    coord_desloc = []
    for i in range(nn):

        coord_desloc.append([coord[i][0] + U[3*i], coord[i][1] + U[3*i + 1], coord[i][2] + U[3*i + 2]])

    # Organiza os pontos dos elementos originais e finais
    X_max = []
    X_min = []
    Y_max = []
    Y_min = []
    Z_max = []
    Z_min = []

    Xd_max = []
    Xd_min = []
    Yd_max = []
    Yd_min = []
    Zd_max = []
    Zd_min = []

    Xm = []
    Ym = []
    Zm = []

    Xmd = []
    Ymd = []
    Zmd = []
    for i in range(ne):

        # Coordenadas dos nós originais
        X, Y, Z, _ = coordenadas(conect[i], coord)

        xm = sum(X)/len(X)
        ym = sum(Y)/len(Y)
        zm = sum(Z)/len(Z)

        Xm.append(xm)
        Ym.append(ym)
        Zm.append(zm)

        X_max.append(max(X))
        X_min.append(min(X))
        Y_max.append(max(Y))
        Y_min.append(min(Y))
        Z_max.append(max(Z))
        Z_min.append(min(Z))

        # Coordenadas dos nós deslocados
        Xd, Yd, Zd, _ = coordenadas(conect[i], coord_desloc)

        xmd = sum(Xd)/len(Xd)
        ymd = sum(Yd)/len(Yd)
        zmd = sum(Zd)/len(Zd)

        Xmd.append(xmd)
        Ymd.append(ymd)
        Zmd.append(zmd)

        Xd_max.append(max(Xd))
        Xd_min.append(min(Xd))
        Yd_max.append(max(Yd))
        Yd_min.append(min(Yd))
        Zd_max.append(max(Zd))
        Zd_min.append(min(Zd))

        # Definindo as arestas do cubo
        faces = [[coord[conect[i][0]], coord[conect[i][1]], coord[conect[i][2]], coord[conect[i][3]]],  # face inferior
                 [coord[conect[i][4]], coord[conect[i][5]], coord[conect[i][6]], coord[conect[i][7]]],  # face superior
                 [coord[conect[i][0]], coord[conect[i][1]], coord[conect[i][5]], coord[conect[i][4]]],  # face frente
                 [coord[conect[i][2]], coord[conect[i][3]], coord[conect[i][7]], coord[conect[i][6]]],  # face traseira
                 [coord[conect[i][1]], coord[conect[i][2]], coord[conect[i][6]], coord[conect[i][5]]],  # face direita
                 [coord[conect[i][4]], coord[conect[i][7]], coord[conect[i][3]], coord[conect[i][0]]]]  # face esquerda
        
        faces_desloc = [[coord_desloc[conect[i][0]], coord_desloc[conect[i][1]], coord_desloc[conect[i][2]], coord_desloc[conect[i][3]]],  # face inferior
                        [coord_desloc[conect[i][4]], coord_desloc[conect[i][5]], coord_desloc[conect[i][6]], coord_desloc[conect[i][7]]],  # face superior
                        [coord_desloc[conect[i][0]], coord_desloc[conect[i][1]], coord_desloc[conect[i][5]], coord_desloc[conect[i][4]]],  # face frente
                        [coord_desloc[conect[i][2]], coord_desloc[conect[i][3]], coord_desloc[conect[i][7]], coord_desloc[conect[i][6]]],  # face traseira
                        [coord_desloc[conect[i][1]], coord_desloc[conect[i][2]], coord_desloc[conect[i][6]], coord_desloc[conect[i][5]]],  # face direita
                        [coord_desloc[conect[i][4]], coord_desloc[conect[i][7]], coord_desloc[conect[i][3]], coord_desloc[conect[i][0]]]]  # face esquerda
        
        if plot_original is True:
            # Adicionando as faces ao gráfico
            ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='blue', alpha=0.25))

            # Adicionando rótulos
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            # Adicionando rótulos aos vértices (nós)
            if plot_nodes_original is True:
                for j, (x, y, z) in enumerate(coord):
                    ax.text(x, y, z, f'{j + 1}', color='black', fontsize=10, ha='center', va='center')


        if plot_desloc is True:
            # Adicionando as faces ao gráfico
            axd.add_collection3d(Poly3DCollection(faces_desloc, facecolors='lime', linewidths=1, edgecolors='green', alpha=0.25))

            # Adicionando rótulos
            axd.set_xlabel('X')
            axd.set_ylabel('Y')
            axd.set_zlabel('Z')


            # Adicionando rótulos aos vértices (nós)
            if plot_nodes_desloc is True:
                for j, (x, y, z) in enumerate(coord_desloc):
                    axd.text(x, y, z, f'{j + 1}', color='black', fontsize=10, ha='center', va='center')


    if plot_original is True:
        # Ajuste dos limites dos eixos
        ax.set_xlim([min(X_min) + 0.4*min(X_min), max(X_max) + 0.4*max(X_max)])
        ax.set_ylim([min(Y_min) + 0.4*min(Y_min), max(Y_max) + 0.4*max(Y_max)])
        ax.set_zlim([min(Z_min) + 0.4*min(Z_min), max(Z_max) + 0.4*max(Z_max)])

    if plot_desloc is True:
        # Ajuste dos limites dos eixos
        axd.set_xlim([min(Xd_min) + 0.4*min(Xd_min), max(Xd_max) + 0.4*max(Xd_max)])
        axd.set_ylim([min(Yd_min) + 0.4*min(Yd_min), max(Yd_max) + 0.4*max(Yd_max)])
        axd.set_zlim([min(Zd_min) + 0.4*min(Zd_min), max(Zd_max) + 0.4*max(Zd_max)])


    

