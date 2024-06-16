import numpy as np


def mesh(Lx, Ly, Lz, nx, ny, nz):

    nn_plane = (nx + 1)*(ny + 1)

    x = np.linspace(0, Lx, nx + 1)
    y = np.linspace(0, Ly, ny + 1)
    z = np.linspace(0, Lz, nz + 1)

    p = []
    for i in z:
        for j in y:
            for k in x:
                p.append([k, j, i])

    conect = []
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):

                no1 = (i + 1) + ((j + 1) - 1)*(nx + 1) + ((k + 1) - 1)*(nn_plane) - 1
                no2 = ((i + 1) + 1) + ((j + 1) - 1)*(nx + 1) + ((k + 1) - 1)*(nn_plane) - 1
                no3 = ((i + 1) + 1) + ((j + 1))*(nx + 1) + ((k + 1) - 1)*(nn_plane) - 1
                no4 = (i + 1) + ((j + 1))*(nx + 1) + ((k + 1) - 1)*(nn_plane) - 1

                no5 = (i + 1) + ((j + 1)-1)*(nx + 1) + ((k + 1))*(nn_plane) - 1
                no6 = ((i + 1) + 1) + ((j + 1) - 1)*(nx + 1) + ((k + 1))*(nn_plane) - 1
                no7 = ((i + 1) + 1) + ((j + 1))*(nx + 1) + ((k + 1))*(nn_plane) - 1
                no8 = (i + 1) + ((j + 1))*(nx + 1) + ((k + 1))*(nn_plane) - 1

                conect.append([no1, no2, no3, no4, no5, no6, no7, no8])


    return p, conect