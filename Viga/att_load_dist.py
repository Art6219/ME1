import numpy as np


def coord_dist(n, ele, coord, conect, n_ant):

    conexao = conect[ele + n_ant]
    
    x = np.linspace(coord[conexao[0]][0], coord[conexao[1]][0], n + 1)
    y = np.linspace(coord[conexao[0]][1], coord[conexao[1]][1], n + 1)

    i = 1
    while i < len(x) - 1:
        
        coord.insert(coord.index(coord[conexao[0]]) + i, [x[i], y[i]])
        conect.insert(conect.index(conexao) + i, [coord.index(coord[conexao[0]]) + i, coord.index(coord[conexao[0]]) + i + 1])
        
        i += 1

    n_ant = n - 1

    return coord, conect, n_ant


def load_distribuida(L, q1, q2, x):

    f = (q2 - q1)/L*x + q1

    return f


def careg_dist(n, L, q1, q2, ele, load_dist_final, ele_ant):

    passo = np.linspace(0, L, n + 1)

    load_dist_novo = []
    for j in range(len(passo) - 1):

        f1 = load_distribuida(L, q1, q2, passo[j])
        f2 = load_distribuida(L, q1, q2, passo[j + 1])

        load_dist_novo.append([ele_ant + ele + j, f1, f2])

    for j in range(len(load_dist_novo)):
    
        load_dist_final.append(load_dist_novo[j])

    ele_ant = load_dist_novo[-1][0]

    return load_dist_final, ele_ant


def att_load_dist(coord, conect, load_dist):

    L = []
    for i in range(len(load_dist)):

        # Seleciona os nós do elemento
        node1 = conect[i][0]
        node2 = conect[i][1]

        # Coordenadas do elemento
        x1 = coord[node1][0]
        y1 = coord[node1][1]

        x2 = coord[node2][0]
        y2 = coord[node2][1]

        # Calcula comprimento do elemento
        dx = x2 - x1
        dy = y2 - y1

        L.append(np.sqrt(dx ** 2 + dy ** 2))

    n_ant = 0
    ele_ant = 0
    load_dist_final = []
    conect_final = []
    for i in range(len(load_dist)):
        coord, conect, n_ant = coord_dist(load_dist[i][3], load_dist[i][0], coord, conect, n_ant)
        load_dist_final, ele_ant = careg_dist(load_dist[i][3], L[i], load_dist[i][1], load_dist[i][2], load_dist[i][0], load_dist_final, ele_ant)

    for i in range(len(coord) - 1):
        conect_final.append([i, i + 1])

    return coord, conect_final, load_dist_final

