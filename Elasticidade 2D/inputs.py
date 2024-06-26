import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 3

# Lista dos problemas
if Problema == 1:
    
      # Inputs 1
      coord = [[0, 0],              # Coordenadas dos Pontos
               [3, 0],
               [6, 0],
               [9, 0],
               [0, 5],
               [3, 5],
               [6, 5],
               [9, 5]]

      conect = [[0, 1, 5, 4],             # Conectividades
                [1, 2, 6, 5],
                [2, 3, 7, 6]]

      ele_type = [1, 1, 1]                # Tipo de elemento (1: isoparamétrico bilinear; 2: bolha; 3: CST)

      esp = 0.05                             # Espessura

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "EPT"                         # Hipótese

      cc = [[0, 1, 0],                    # Condições de Contorno [Nó, GL, Valor]
            [0, 2, 0],
            [4, 1, 0],
            [4, 2, 0]]

      Loads = [[3, 1, 1],                 # Forças [Nó, GL, Valor]
               [7, 1, 1]]       
      
elif Problema == 2:
    
      # Inputs 1
      coord = [[0, 0],              # Coordenadas dos Pontos
            [3, 0],
            [6, 0],
            [9, 0],
            [0, 5],
            [3, 5],
            [6, 5],
            [9, 5]]

      conect = [[0, 1, 5, 4],             # Conectividades
                  [1, 2, 6, 5],
                  [2, 3, 7, 6]]

      ele_type = [2, 2, 2]                # Tipo de elemento (1: isoparamétrico bilinear; 2: bolha; 3: CST)

      esp = 0.05                             # Espessura

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "EPT"                         # Hipótese

      cc = [[0, 1, 0],                    # Condições de Contorno [Nó, GL, Valor]
            [0, 2, 0],
            [4, 1, 0],
            [4, 2, 0]]

      Loads = [[3, 2, 0.2]]                 # Forças [Nó, GL, Valor]


elif Problema == 3:
    
      # Inputs 1
      coord = [[0, 0],              # Coordenadas dos Pontos
               [0, 2],
               [0, 4],
               [0, 6],
               [2, 0],
               [2, 2],
               [2, 4],
               [2, 6],
               [4, 0],
               [4, 2],
               [4, 4],
               [4, 6],
               [6, 2],
               [6, 4],
               [8, 2],
               [8, 4],
               [10, 3]]

      conect = [[0, 4, 5, 1],             # Conectividades
                [1, 5, 6, 2],
                [2, 6, 7, 3],
                [4, 8, 9, 5],
                [5, 9, 10, 6],
                [6, 10, 11, 7],
                [8, 12, 9],
                [9, 12, 13, 10],
                [10, 13, 11],
                [12, 14, 15, 13],
                [14, 16, 15]]

      ele_type = [2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3]                # Tipo de elemento (1: isoparamétrico bilinear; 2: bolha; 3: CST)

      esp = 0.05                             # Espessura

      nn = len(coord)                     # Número de Nós
      ne = len(conect)                    # Número de Elementos

      E = 100                           # Módulo de Elasticidade
      v = 0                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "EPT"                         # Hipótese

      cc = [[0, 1, 0],                    # Condições de Contorno [Nó, GL, Valor]
            [0, 2, 0],
            [3, 1, 0],
            [3, 2, 0]]

      Loads = [[16, 2, 0.1]]                 # Forças [Nó, GL, Valor]


# Chama a função main
# Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, cc, VE, Vv, hip, esp)
Ua1, eps, sigmas = main(coord, conect, Loads, cc, VE, Vv, hip, esp, ele_type)

print('Resolução por Lagrange')
print(Ua1)
print('------------------------------------------------------')
print('Tensões nos elementos')
print(sigmas)
print('------------------------------------------------------')
print('Deformação dos elementos')
print(eps)
print('------------------------------------------------------')

plt.show()