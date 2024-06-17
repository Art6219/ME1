import numpy as np
import matplotlib.pyplot as plt

from main import main
from mesh import mesh


# Seleciona qual problema será rodado
Problema = 3

# Lista dos problemas
if Problema == 1:
    
      # Inputs 1
      coord = [[1, -1, -1],
               [1, 1, -1],
               [-1, 1, -1],
               [-1, -1, -1],
               [1, -1, 1],
               [1, 1, 1],
               [-1, 1, 1],
               [-1, -1, 1],
               
               [1, 3, -1],
               [-1, 3, -1],
               [1, 3, 1],
               [-1, 3, 1]]

      conect = [[0, 1, 2, 3, 4, 5, 6, 7],
                [1, 8, 9, 2, 5, 10, 11, 6]]             # Conectividades

      ele_type = [1, 1]                # Tipo de elemento (1: isoparamétrico trilinear; 2: bolha; 3: CST)

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "3D"                         # Hipótese

      cc = [[0, 1, 0],                    # Condições de Contorno [Nó, GL, Valor]
            [0, 2, 0],
            [0, 3, 0],
            [1, 1, 0],
            [1, 2, 0],
            [1, 3, 0]]

      Loads = [[6, 2, 0.1],                 # Forças [Nó, GL, Valor]
               [7, 2, 0.1]]       
      
elif Problema == 2:
    
      # Inputs 1
      coord = [[1, 0, 0],
               [2, 0, 0],
               [3, 0, 0],
               [4, 0, 0],

               [1, 1, 0],
               [2, 1, 0],
               [3, 1, 0],
               [4, 1, 0],

               [1, 2, 0],
               [2, 2, 0],
               [3, 2, 0],
               [4, 2, 0],


               [1, 0, 1],
               [2, 0, 1],
               [3, 0, 1],
               [4, 0, 1],

               [1, 1, 1],
               [2, 1, 1],
               [3, 1, 1],
               [4, 1, 1],

               [1, 2, 1],
               [2, 2, 1],
               [3, 2, 1],
               [4, 2, 1],]

      conect = [[0, 1, 5, 4, 12, 13, 17, 16],
                [1, 2, 6, 5, 13, 14, 18, 17],
                [2, 3, 7, 6, 14, 15, 19, 18],
                [4, 5, 9, 8, 16, 17, 21, 20],
                [5, 6, 10, 9, 17, 18, 22, 21],
                [6, 7, 11, 10, 18, 19, 23, 22]]             # Conectividades

      ele_type = [1, 1, 1, 1, 1, 1, 1]                # Tipo de elemento (1: isoparamétrico trilinear; 2: bolha; 3: CST)

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "3D"                         # Hipótese

      # Condições de Contorno [Nó, GL, Valor]
      cc = [[0, 1, 0],                    
            [0, 2, 0],
            [0, 3, 0]]

      # Forças [Nó, GL, Valor]
      Loads = [[1, 1, 0]]    


elif Problema == 3:

      # Tamanho do paralelepipedo
      Lx = 8
      Ly = 1
      Lz = 4

      # Núemero de elementos
      nx = 20    
      ny = 1
      nz = 40

      coord, conect = mesh(Lx, Ly, Lz, nx, ny, nz)

      tipo = 2                                        # Tipo de elemento (1: isoparamétrico trilinear; 2: bolha; 3: CST)
      ele_type = tipo * np.ones(len(conect))                

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100000                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "3D"                         # Hipótese

      cc = []
      for i in range(len(coord)):
            if coord[i][0] == 0:
                  cc.append([i, 1, 0])
                  cc.append([i, 2, 0])
                  cc.append([i, 3, 0])

      # Forças [Nó, GL, Valor]
      Loads = []
      for i in range(len(coord)):
            if coord[i][0] == Lx and coord[i][2] == Lz:
                  Loads.append([i, 3, 1])

      desloc = []
      for i in range(len(coord)):
            if coord[i][0] == Lx:
                  desloc.append(i)


# Chama a função main
# Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, cc, VE, Vv, hip, esp)
Ua1, eps, sigmas = main(coord, conect, Loads, cc, VE, Vv, hip, ele_type)

# Cálculo Flecha
P = 2
I = Ly*Lz**3/12
v = P*Lx**3/(3*E*I)

print(f"Deslocamentos em x = L")
desloc_mid = []
for i in range(len(desloc)):
      # print(f"{i + 1}:{Ua1[3*desloc[i] + 2]}")
      desloc_mid.append(Ua1[3*desloc[i] + 2])

print('------------------------------------------------------')

print(f"flecha FEM: {desloc_mid[int(len(desloc_mid)/2)]}")

print('------------------------------------------------------')

print(f"flecha analítica: {v}")

# print('Resolução por Lagrange')
# print(Ua1)
# print('------------------------------------------------------')
# print('Tensões nos elementos')
# print(sigmas)
# print('------------------------------------------------------')
# print('Deformação dos elementos')
# print(eps)
# print('------------------------------------------------------')

plt.show()