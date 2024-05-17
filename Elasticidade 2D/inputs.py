import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 1

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
      v = 0.3                               # Coeficiente de Poisson

      VE = E * np.ones(ne)
      Vv = v * np.ones(ne)

      hip = "EPT"                         # Hipótese

      cc = [[0, 1, 0],                    # Condições de Contorno [Nó, GL, Valor]
            [0, 2, 0],
            [4, 1, 0],
            [4, 2, 0]]

      Loads = [[3, 1, 1],                 # Forças [Nó, GL, Valor]
                  [7, 1, 1]]       


# Chama a função main
# Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, cc, VE, Vv, hip, esp)
Ua1, Ua2, Ua3 = main(coord, conect, Loads, cc, VE, Vv, hip, esp, ele_type)

print('Resolução por Lagrange')
print(Ua1)
print('------------------------------------------------------')
print('Resolução excluindo as linhas/colunas com restrições')
print(Ua2)
print('------------------------------------------------------')
print('Resolução zerando linhas/colunas com restrições')
print(Ua3)
# print('------------------------------------------------------')
# print('Tensões nos elementos')
# print(Sigma)
# print('------------------------------------------------------')

plt.show()