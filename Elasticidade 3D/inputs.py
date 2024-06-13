import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 1

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
    
      pass


# Chama a função main
# Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, cc, VE, Vv, hip, esp)
Ua1, eps, sigmas = main(coord, conect, Loads, cc, VE, Vv, hip, ele_type)

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